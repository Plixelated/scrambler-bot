#!/bin/bash

if [ ! -d "scrambler-bot" ]; then
    git clone https://github.com/Plixelated/scrambler-bot.git 
fi

cd scrambler-bot

git checkout docker 
git pull origin docker

if [ ! -f "$DISCORD_TOKEN_FILE" ]; then
    echo "Token file not found: $DISCORD_TOKEN_FILE"
    exit 1
fi

DISCORD_TOKEN=$(cat $DISCORD_TOKEN_FILE)

export DISCORD_TOKEN

python /app/scrambler-bot/bot/main.py