# Various tiny ai-powered terminal helpers

## Prerequisites
Before you begin, ensure you have the following installed on your machine:

Python 3.x

- pip (Python package installer)
- virtualenv

## Setup

1. **Clone the Repository**

Clone the repository into your home folder using the following commands:

```bash
git clone git@github.com:MindWrapper/ai-tools.git  ~/ai-tools &&
cd ~/ai-tools
```

2. **Setup virtual env and install python depdenencies**

```bash
python3 -m venv venv &&
source venv/bin/activate &&
pip install -r requirements.txt &&
deactivate
```

3. **Integrate with Shell**

Update `~/.zprofile`, the same should work for `~/.bashrc` or  `~/.bash_profile`

```bash
echo 'ai() { ~/ai-tools/venv/bin/python ~/ai-tools/aicmd.py "$@"; }' >> ~/.zprofile  &&
source ~/.zprofile
```

4. **Setup Open AI secrets**

Obtain api key from https://platform.openai.com/api-keys

```bash
mkdir -p ~/.secrets/aicmd && touch ~/.secrets/aicmd/.env
```

```bash
echo "OPEN_AI_KEY=your_key" >>  ~/.secrets/aicmd/.env
```

# Usage

Example command:

```bash
ai "count how many time 'AI Command Line Assistant' can be found in the current dir"
```

Output:

`grep -ri "AI Command Line Assistant" . | wc -l`


# License

This project is licensed under the MIT License.

## Troubleshooting

### Common Errors
Ensure you have an active API account with OpenAI and sufficient credits.

#### 1. RateLimitError (Error Code: 429)
This error indicates you've exceeded your OpenAI API quota. To resolve this, verify your current API usage and consider options like upgrading your plan or optimizing your API calls. For more information on rate limits and how to manage them, refer to [OpenAI Error Codes](https://platform.openai.com/docs/guides/error-codes/api-errors).

#### 2. NotFoundError (Error Code: 404)
This error occurs when the `gpt-4` model is either not available or you don't have access to it. Check [Accessing GPT-4](https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4).





