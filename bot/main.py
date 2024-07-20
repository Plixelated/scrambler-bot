import os
import discord
from discord import app_commands
from typing import Optional
from responder import responder

token = os.getenv("DISCORD_TOKEN")

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced=False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user} has logged in')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(
    name="echo", 
    description="Echo a comment", 
)
@app_commands.describe(
    echo="Enter Text to be Scrambled",
    #scramble="What are the chances the text will be scrambled?",
    alter="What Percent of the Text is Scrambled?",
)
async def self(
    interaction: discord.Interaction, 
    echo: str,
    #scramble: Optional[int],
    alter: Optional[int],
    ):
        r = responder()

        if not alter:
             r.respond(echo, 0, 0)
        else:
            echo = r.respond(echo, 100, alter)
        await interaction.response.send_message(f'{echo}')


if __name__ == '__main__':
    client.run(token)