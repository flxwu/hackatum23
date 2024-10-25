import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI({
	apiKey: process.env.OPENAI_API_KEY,
});

const chunkToPrompt = (
  chunk
) => `I am a DevOps engineer analyzing these logs below.
Help me identify patterns or issues that could impact system performance, reliability, security, particularly around SSH.
Give me a short, concise list of bullet points. 
${chunk}`;

const requestCompletion = async (chunk) => {
  const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: "user", content: chunkToPrompt(chunk) }],
    model: "gpt-3.5-turbo-1106",
  });
  return chatCompletion.choices[0].message.content;
};

const splitContext = (context) => {
  const chunks = [];
  const overlap = 50;
  let start = 0;
  while (start < context.length) {
    let end = Math.min(start + 16000, context.length);
    chunks.push(context.substring(start, end));
    if (end == context.length) break;
    start = end - overlap;
  }
  return chunks;
};

(async () => {
  // Read file
  const fileContent = fs.readFileSync("./data/test_log1 copy.out").toString();
  const strippedContent = fileContent
    .split("\n")
    .map((line) => line.split(" ").slice(4))
    .join("\n");
  const chunks = splitContext(strippedContent);

  // Request completion
  const results = await Promise.allSettled(chunks.map(requestCompletion));
  console.log(results.length, results);

  const summaries = results.map((result) => result.value).join("\n");
  console.log(summaries);

  const summaryOfSummaries = await openai.chat.completions.create({
    messages: [
      {
        role: "user",
        content: `I am a Staff DevOps engineer with IQ 150. Below is a summary analysis of logs.
        Extract the most important information from the summary, in particular issues impacting system performance, reliability, security, particularly around SSH.
        Give me a short, concise list of bullet points.
        ${summaries}`,
      },
    ],
    temperature: 0.1,
    model: "gpt-3.5-turbo-1106",
  });

  console.log(
    "\n\n\n[TOTAL RESULT]: ",
    summaryOfSummaries.choices[0].message.content
  );
})();
