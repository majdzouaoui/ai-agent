import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
import json
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY is not set")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
parser = argparse.ArgumentParser(description="chatbot")
parser.add_argument("user_prompt", type=str, help="user input")
parser.add_argument("--verbose", action="store_true", help="enable verbose output")
args = parser.parse_args()
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

for i in range(20):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )
    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            messages.append(result_message)

            if not result_message["content"]:
                raise Exception("Tool call returned empty content")

            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print(message.content)
        break
else:
    print("Maximum iterations reached without a final response.")

if args.verbose:
    print("User prompt:", messages[1]["content"])
    if response.usage is None:
        raise RuntimeError("info not available ")
    else:
        print("Prompt tokens:", response.usage.prompt_tokens)
        print("Response tokens:", response.usage.completion_tokens)
