import LogInput
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import requests
import logging
import contextlib
from http.client import HTTPConnection
import json
import aiohttp
import HTTPClient
import OpenAIHTTPClient
from math import floor

MAX_CHUNK_LENGTH = 16385
MAX_OUTPUT_LENGTH = 512


def split_context(context, overlap=50, max_length=MAX_CHUNK_LENGTH):
    """
    Function for splitting context into overlapping chunks.

    param context: This is the text that you want to split into chunks. 
    The function will split this text based on the max_length and overlap parameters.

    param overlap (default=50): This is the number of characters that will overlap between each chunk. 
    This is used to ensure that the context is not cut off in the middle of a sentence, which could make the text difficult to understand.

    param max_length (default=512): This is the maximum length of each chunk. 
    The function will split the context into chunks of this length, with the exception of the last chunk, which may be shorter.

    The function returns a list of chunks, where each chunk is a string of text from the context. 
    The chunks are created by starting at the beginning of the context and moving forward max_length
    characters at a time, with an overlap of overlap characters between each chunk.
    """

    chunks = []
    start = 0
    while start < len(context):
        end = min(start + max_length, len(context))
        chunks.append(context[start:end])
        if end == len(context):
            break
        start = end - overlap
    return chunks


def prompt_to_summarize_logs(input):
    return f"""
            I am a DevOps engineer analyzing these logs below.
            Help me identify patterns or issues that could impact system performance, reliability, security, particularly around SSH.
            Give me a very short, concise list of bullet points. 
            {input}
        """


def prompt_to_summarize_summaries(input):
    return f"""
            I am a DevOps engineer analyzing these summaries of logs below.
        Help me summarize the most important parts regarding system performance, reliability, security, particularly around SSH.
        Give me a very short, concise list of bullet points. 
            {input}
        """


def deprecated_prompt_body_to_summarize_logs(input):
    return {
        "input": f"""
                    [INST] I am a DevOps engineer analyzing these logs below.
            Help me identify patterns or issues that could impact system performance, reliability, security, particularly around SSH.
            Give me a very short, concise list of bullet points. 
            {input} [/INST]
                    """,
        "max_new_tokens": MAX_CHUNK_LENGTH,
    }


def deprecated_prompt_body_to_summarize_summaries(input):
    return {
        "input": f"""
                [INST] I am a DevOps engineer analyzing these summaries of logs below.
        Help me summarize the most important parts regarding system performance, reliability, security, particularly around SSH.
        Give me a very short, concise list of bullet points. 
        {input} [/INST]
                """,
        "max_new_tokens": MAX_CHUNK_LENGTH,
    }


async def summarize_many_chunks(input_chunks, input_to_prompt_body) -> [str]:
    """
    Summarizes many chunks of text in parallel.
    """

    # Get API responses for all chunks
    # json_responses = await HTTPClient.parallel_post(post_bodies)

    prompts = []
    for input in input_chunks:
        prompts.append(input_to_prompt_body(input))
    summaries = await OpenAIHTTPClient.request_completions_for(prompts)

    # Parses an API response to a single summary string
    # def response_to_summary(response) -> str:
    #     tokens_generated = response["inference_status"]["tokens_generated"]
    #     results = response["results"]
    #     # results is a list of dicts, so join them together
    #     summary = "\n".join(
    #         list(map(lambda r: r["generated_text"], results)))
    #     # sometimes, the bullet points will be inlined with the asterisk
    #     summary = "\n* ".join(summary.split(" * "))
    #     print(
    #         f"[LOGLENS] API returned {tokens_generated} tokens with result: ", summary)
    #     return summary
    # summaries = list(map(response_to_summary, json_responses))

    return summaries


async def summarize_summaries(input_str):
    chunks = split_context(input_str)
    outputs = await summarize_many_chunks(chunks, prompt_to_summarize_logs)
    # 16385/512 = 32
    # number of new chunks: len(outputs)/8

    print("[LOGLENS] Summarizing summaries")
    while len(outputs) > 1:
        number_chunks = floor(
            (len(outputs)/(MAX_CHUNK_LENGTH/MAX_CHUNK_LENGTH))) + 1
        outputs_temp = []
        for i in range(number_chunks):
            outputs_temp.append("".join(outputs[i:i+32]))
        outputs = await summarize_many_chunks(
            outputs_temp, prompt_to_summarize_summaries)

    return outputs[0]
