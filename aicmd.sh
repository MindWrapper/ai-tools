#!/bin/bash

AI_COMMAND="$1"

source ~/.secrets/aicmd/.env

PROMPT="print command that does '${AI_COMMAND}'.
If user asks to search or find something, then make sure to include hidden files.
If user doesn't specify the scope of search command, then use current directory.
Output should contain command only, I can paste into terminal. No comments or anything else.
Output should be a single line."

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
if [ -n "$COMMAND" ]; then
    echo "$COMMAND"
else
    echo "Cannot generate command. Try another prompt."
fi
