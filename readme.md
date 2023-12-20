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

update ~/.zprofile, the same should work for `~/.bashrc` or  `~/.bash_profile`

```bash
echo 'ai() { ~/ai-tools/venv/bin/python ~/ai-tools/aicmd.py "$@"; }' >> ~/.zprofile  &&
source ~/.zprofile
```

1. Setup Open AI secrets

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
