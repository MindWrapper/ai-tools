# Various tiny ai-powered terminal helpers

## Prerequisites
Before you begin, ensure you have the following installed on your machine:

Python 3.x

- pip (Python package installer)
- virtualenv

## Setup

```bash
git clone git@github.com:MindWrapper/ai-tools.git ~/ai-tools

cd ~/ai-tools

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

chmod +x aicmd.py
```

### Integrate with the Shell

```bash

# update .zprofile, the same should work for .bashrc or  ~/.bash_profile
echo 'ai() { ~/ai-tools/venv/bin/python ~/ai-tools-tool/aicmd.py "$@"; }' >> ~/.zprofile 

source ~/.zprofile

```bash
deactivate
mkdir -p ~/.secrets/aicmd && touch ~/.secrets/aicmd/.env
```

Obtain api key from https://platform.openai.com/api-keys

```bash
echo "OPEN_AI_KEY=your_key" >>  ~/.secrets/aicmd/.env
```

# Usage

Example command:

`ai "count how many times 'AI Command Line Assistant' can be found in the current dir"`

Output:

`grep -ri "AI Command Line Assistant" . | wc -l`


# License
This project is licensed under the MIT License.
