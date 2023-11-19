# Various tiny ai-powered terminal helpers

Setup:

```code
git clone git@github.com:MindWrapper/ai-tools.git ~/ai-tools
echo "ai() { python ~/ai-tools/aicmd.py; }" >> ~/.zprofile  # Use ~/.bashrc or ~/.bash_profile for bash
mkdir -p ~/.secrets/aicmd && touch ~/.secrets/aicmd/.env
# obtain api key from https://platform.openai.com/api-keys
echo "OPEN_AI_KEY=your_key" >>  ~/.secrets/aicmd/.env
source ~/.zprofile  # Or source your bash profile file
```

# Usage

Example command:
`ai "count occurrences of word 'ai' in all files"`

Output:

`grep -rohIi '\bai\b' . | wc -w`