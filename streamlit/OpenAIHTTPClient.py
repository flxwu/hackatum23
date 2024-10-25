from openai import AsyncOpenAI
import asyncio
client = AsyncOpenAI()

async def __request_completion__(prompt) -> str:
    print("[LOGLENS] Requesting completion for prompt")
    completion = await client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print("[LOGLENS] Prompt returned result ",
          completion.choices[0].message.content)
    return completion.choices[0].message.content


async def request_completions_for(prompts) -> [str]:
    return await asyncio.gather(*[__request_completion__(p) for p in prompts])
