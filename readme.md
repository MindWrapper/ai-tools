# AI-Powered Terminal Helpers

## Usage

### Use-case 1: Find Appropriate Shell Command

```bash
ai "count how many times 'AI Command Line Assistant' can be found in the current dir"
```

Output:

`grep -ri "AI Command Line Assistant" . | wc -l`

### Use-case 2: Review File

Note: Currently, only Markdown files are supported.

```bash
review ./readme.md
```

Output:

```
Reviewing Markdown file: ./readme.md
Modified Markdown file created at: /var/folders/yk/rk3pptpd609d1y8lcfy6n1vm0000gn/T/tmpdl5dx9c4.modified.md
To compare using Visual Studio Code, use the following command:
code --diff ./readme.md /var/folders/yk/rk3pptpd609d1y8lcfy6n1vm0000gn/T/tmpdl5dx9c4.modified.md
```

`code` is an alias for Visual Studio Code. See [Launching from the command line](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line).

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip
- virtualenv

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:MindWrapper/ai-tools.git  ~/ai-tools
cd ~/ai-tools
```

### 2. Setup Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

### 3. Integrate with Shell

Update `~/.zprofile`. This should also work for `~/.bashrc` or  `~/.bash_profile`.

Add the following lines if they are missing:

```bash
ai() { ~/ai-tools/venv/bin/python ~/ai-tools/aicmd.py "$@"; }
review() { ~/ai-tools/venv/bin/python ~/ai-tools/review.py "$@"; }
```

Then, run:

```bash
source ~/.zprofile
```

### 4. Setup OpenAI Secrets

Get your API key from [OpenAI API Keys](https://platform.openai.com/api-keys).

```bash
mkdir -p ~/.secrets/aicmd && touch ~/.secrets/aicmd/.env
echo "OPEN_AI_KEY=your_key" >>  ~/.secrets/aicmd/.env
```

## License

This project is licensed under the MIT License.

## Troubleshooting

### Common Errors

Ensure you have an active API account with OpenAI and sufficient credits.

#### 1. RateLimitError (Error Code: 429)

This error indicates you've exceeded your OpenAI API quota. Check your current API usage and consider upgrading your plan or optimizing your API calls. For more information, refer to [OpenAI Error Codes](https://platform.openai.com/docs/guides/error-codes/api-errors).

#### 2. NotFoundError (Error Code: 404)

This error occurs when the `gpt-4` model is not available or you don't have access to it. Check [Accessing GPT-4](https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4).