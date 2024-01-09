import argparse
from dotenv import load_dotenv
from openai import OpenAI
import os

def get_completion(prompt, model):

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPEN_AI_KEY")
    )

    messages = [{"role": "user", "content": prompt}]

    response =  client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description='AI Command Line Assistant')
    parser.add_argument('command', help='Command to process')
    args = parser.parse_args()

    home_dir = os.path.expanduser("~")
    dotenv_path = os.path.join(home_dir, ".secrets", "aicmd", ".env")
    load_dotenv(dotenv_path)

    ai_command = args.command

    prompt = f"""
Determine the appropriate shell command based on '{ai_command}':
1. If the user requests a search or find operation, include hidden files by default, unless explicitly stated otherwise.
2. In cases where the user does not specify a search command or the scope of the search, default to the current directory.
3. For git-related requests, ensure the response strictly pertains to git commands.
4. When asked to find a pattern in files, default to case-insensitive matching, unless the user requests case sensitivity.
5. Output should be a single line and signle command. No eplanation or justification is required.
    """

    result = get_completion(prompt, model="gpt-4")
   
    if result is not None:
        print(result)
    else:
        print("Can not generate command. Try another promt.")

if __name__ == "__main__":
    main()
