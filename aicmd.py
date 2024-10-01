import argparse
from dotenv import load_dotenv
from openai import OpenAI
import os
import platform

def get_completion(prompt, model):

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPEN_AI_KEY")
    )

    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
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

    # Detect the operating system
    operating_system = platform.system().lower()

    if 'windows' in operating_system:
        os_specific_info = "Use Windows-specific commands (e.g., `dir`, `findstr`, `git`) if applicable."
    elif 'darwin' in operating_system:  # MacOS is identified as 'darwin'
        os_specific_info = "Use Mac-specific commands (e.g., `ls`, `grep`, `git`) if applicable."
    else:
        os_specific_info = "Use Linux/Unix commands by default."

    prompt = f"""
Determine the appropriate shell command based on '{ai_command}':
1. {os_specific_info}
2. If the user requests a search or find operation, include hidden files by default, unless explicitly stated otherwise.
3. In cases where the user does not specify a search command or the scope of the search, default to the current directory.
4. For git-related requests, ensure the response strictly pertains to git commands.
5. When asked to find a pattern in files, default to case-insensitive matching, unless the user requests case sensitivity.
6. Output must be a single command without quotes and without explanations.
    """

    result = get_completion(prompt, model="gpt-4o")
   
    if result is not None:
        print(result)
    else:
        print("Cannot generate command. Try another prompt.")

if __name__ == "__main__":
    main()
