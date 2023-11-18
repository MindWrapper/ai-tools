import openai
import argparse
from dotenv import load_dotenv
import os

# Function to call OpenAI API
def query_openai(prompt):
    # Add your API key here
    home_dir = os.path.expanduser("~")
    dotenv_path = os.path.join(home_dir, ".secrets", "aicmd", ".env")
    load_dotenv(dotenv_path)
    openai.api_key = os.environ.get('OPEN_AI_KEY')

    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      max_tokens=100
    )
    return response.choices[0].text.strip()

# Main function for the CLI
def main():
    parser = argparse.ArgumentParser(description='AI Command Line Assistant')
    parser.add_argument('command', help='Command to process')
    args = parser.parse_args()

    ai_command = args.command
    if ai_command.startswith("ai: "):
        ai_command = ai_command.replace("ai: ", "")
        result = query_openai(ai_command)
        print(result)
    else:
        print("Command must start with 'ai: '")

if __name__ == "__main__":
    main()
