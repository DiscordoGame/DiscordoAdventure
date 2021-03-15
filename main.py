from dbhandle import DatabaseHandle
from common.config import Config
from game.player import Player

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # We only accept messages from TextChannels
        if isinstance(message.channel, discord.TextChannel) and message.content == '!start':
            # Delete the message that the user sent with '!start' in the general channel
            await message.delete();
            # DM the author of message with a greating
            await message.author.send('Hello traveler ' + message.author.name + ".")
            player = Player(message.author.id, message.created_at)
            player.save_to_db()
        elif isinstance(message.channel, discord.DMChannel):
            # Should split on regex with multiple spaces
            parts = message.content.strip().split(' ')
            if len(parts) == 1:
                response = "What " + parts[0] + "??"
            else:
                command = parts[0]
                response = "You really want to \"" + command + "\" " + parts[1] + "?"

            await message.author.send(response)

Config.load_from('config.json')

client = MyClient()
client.run(Config.get_by_key('token'))
