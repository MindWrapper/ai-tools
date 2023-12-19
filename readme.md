# Various tiny ai-powered terminal helpers


## Prerequisites
Before you begin, ensure you have the following installed on your machine:

Python 3.x

- pip (Python package installer)
- virtualenv

Setup:

```bash
git clone git@github.com:MindWrapper/ai-tools.git ~/ai-tools

cd  ~/ai-tools 

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

```
#echo "ai() { python  ~/ai-tools/aicmd.py; }" >> ~/.zprofile  # Or

add `ai` function to `~/.zprofile` (or ~/.bashrc or ~/.bash_profile )

```bash
ai() {
    ~/ai-tools/venv/bin/python ~/ai-tools/aicmd.py "$@"
}
deactivate

mkdir -p ~/.secrets/aicmd && touch ~/.secrets/aicmd/.env
```

Obtain api key from https://platform.openai.com/api-keys

```bash
echo "OPEN_AI_KEY=your_key" >>  ~/.secrets/aicmd/.env
source ~/.zprofile 
```

# Usage

Example command:
`grep -ri "AI Command Line Assistant" . | wc -l`

Output:

`grep -rohIi '\bai\b' . | wc -w`