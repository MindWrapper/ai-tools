import sys
from dotenv import load_dotenv
from openai import OpenAI
import os
import subprocess
import tempfile  

def review_md_file(file_path):
    print(f"Reviewing Markdown file: {file_path}")
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)

    with open(file_path, 'r') as file:
        md_content = file.read()

    prompt = f"""
Output must be the modified file, with all the improvements. Here is a list of instructions you should follow:
1. Don't include explanations, only raw file content.
2. Don't quote the output.
3. Ensure headers are properly used to structure the document clearly.
4. Check that lists are properly formatted and used where appropriate for readability.
5. Verify links are valid and lead to the expected content.
6. Ensure that any code blocks are correctly formatted and syntactically correct for the specified language.
7. Make sure there is an empty line at the end of the file.
8. Enhance readability where necessary, such as splitting long paragraphs or sentences.
9. Check for and correct spelling and grammar mistakes.
10. Include comments to suggest improvements on how to present complex information more clearly.
    """

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user",  "content": md_content}
    ]

    client = OpenAI(
        api_key=os.environ.get("OPEN_AI_KEY")
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0,
    )

    modified_content = response.choices[0].message.content.strip()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".modified.md", mode='w') as modified_file:
        modified_file.write(modified_content)
        modified_file_path = modified_file.name  # Save the path for later use

    return modified_file_path

def is_vscode_installed():
    try:
        subprocess.run(["code", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path-to-file>")
        sys.exit(1)

    file_path = sys.argv[1]

    _, file_extension = os.path.splitext(file_path)

    home_dir = os.path.expanduser("~")
    dotenv_path = os.path.join(home_dir, ".secrets", "aicmd", ".env")
    load_dotenv(dotenv_path)

    if file_extension == '.md':
        modified_file_path = review_md_file(file_path)
        print(f"Modified Markdown file created at: {modified_file_path}")
        if is_vscode_installed():
            print(f"To compare using Visual Studio Code, use the following command:")
            print(f"code --diff {file_path} {modified_file_path}")
        else:
            print("Visual Studio Code is not detected. Please download and install it from https://code.visualstudio.com/,")
            print("or use any other diff tool you have available to compare the files.")
    else:
        print(f"Unsupported file type: {file_extension}")
        sys.exit(1)
