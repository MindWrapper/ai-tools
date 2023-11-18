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
    if ai_command.startswith("ai: "):
        ai_command = ai_command.replace("ai: ", "print command that ")
        ai_command += " use single line to I can copy & paste. include hidden files into the search"
        result = get_completion(ai_command, model="gpt-4")
        print(result)
    else:
        print("Command must start with 'ai: '")

if __name__ == "__main__":
    main()
