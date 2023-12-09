#!/bin/bash

AI_COMMAND="$1"

source ~/.secrets/aicmd/.env

PROMPT="print command that does '${AI_COMMAND}'.
If user asks to search or find something, then make sure to include hidden files.
If user doesn't specify the scope of search command, then use current directory.
Output should contain command only, I can paste into terminal. No comments or anything else.
Output should be a single line and signle command."

RESPONSE=$(curl -s -X POST "https://api.openai.com/v1/chat/completions" \
    -H "Authorization: Bearer $OPEN_AI_KEY" \
    -H "Content-Type: application/json" \
    -d @- <<EOF
{
  "model": "gpt-4",
  "messages": [{"role": "user", "content": "$PROMPT"}],
  "temperature": 0
}
EOF
)

COMMAND=$(echo $RESPONSE | jq -r '.choices[0].message.content')

# Check and display the command
# Check and offer options
if [ -n "$COMMAND" ]; then
    echo "$COMMAND"
    echo "(c)opy or (e)xecute?"
    read -r choice

    case $choice in
        c|C)
            echo "$COMMAND" | pbcopy  # For macOS. Use 'xclip -selection clipboard' or 'xsel --clipboard --input' on Linux
            echo "Command copied to clipboard."
            ;;
        e|E)
            eval "$COMMAND"
            ;;
        *)
            echo "Invalid choice. Exiting."
            ;;
    esac
else
    echo "Cannot generate command. Try another prompt."
fi