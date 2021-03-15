from dbhandle import DatabaseHandle
from common.config import Config
from common.cmd_parser import CmdParser
from game.player import Player

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        p = CmdParser(message.content)
        
        # We only accept messages from TextChannels
        if isinstance(message.channel, discord.TextChannel) and p.is_command:
            if p.get_command() == 'start':
                # Delete the message that the user sent with '!start' in the general channel
                await message.delete();

                author = message.author;
                # DM the author of message with a greating
                await author.send('Hello traveler ' + author.name + ".")

                # TODO(mateusz): Should probably be read from some sort
                # of a file where bot responses are stored to allow 
                # maybe for translation and easier addition of lines
                
                player = Player(author.id, message.created_at)
                if not player.seen_tutorial():
                    tutorial = "To play the game send me two word commands with out the need for the prefixing '!'. Each command has a body like so <verb> <noun>, where verb is the thing you want to do and noun the thing you want to do it with. To get a list of all possible commands send a 'help commands' message."
                    tutorial2 = "To practice your first command you can confirm to me that you understand everything and don't want to see this tutorial anymore. Simply type 'dismiss tutorial'..."
                    await author.send(tutorial)
                    await author.send(tutorial2)
                
                player.save_to_db()                
            elif p.get_command() == 'help':
                msg = "To start the game type !start and I will guide you through everything that you need to know."
                
                await message.channel.send(msg)
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
