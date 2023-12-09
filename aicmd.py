import openai
import argparse
from dotenv import load_dotenv
import os


def get_completion(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]


def main():
    parser = argparse.ArgumentParser(description='AI Command Line Assistant')
    parser.add_argument('command', help='Command to process')
    args = parser.parse_args()

    home_dir = os.path.expanduser("~")
    dotenv_path = os.path.join(home_dir, ".secrets", "aicmd", ".env")
    load_dotenv(dotenv_path)

    openai.api_key = os.environ.get('OPEN_AI_KEY')
    ai_command = args.command

    prompt = f"""
    print command that does '{ai_command}'.
    If user asks to search or find something, then make sure to include hidden files.
    If user doesn't specify the scope of search command, then use current directory.
    Output should contain command only, I can paster into terminal. No comments or anything else.
    Output should be in json object that contains command in 'command' key.
    """

    result = get_completion(prompt, model="gpt-4")
    print(result["command"])

if __name__ == "__main__":
    main()
