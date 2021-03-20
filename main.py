from common.dbhandler import DatabaseHandler
from common.config import Config
from common.cmd_parser import CmdParser
from common.interpreter import CmdInterpreter
from common.langs import Langs
from game.player import Player
from pathlib import Path

import discord

class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        p = CmdParser(message.content)
        author = message.author;
        player = Player(author.id, message.created_at)
        
        # We only accept messages from TextChannels
        if isinstance(message.channel, discord.TextChannel) and p.is_command:
            if p.get_command() == 'start':
                # Delete the message that the user sent with '!start' in the general channel
                await message.delete();

                # DM the author of message with a greating
                await author.send('Hello traveler ' + author.name + ".")

                player.save_to_db()
                
        elif isinstance(message.channel, discord.DMChannel):
            if not player.seen_tutorial():
                tutorial = Langs.get_text("tutorial_intro")
                tutorial2 = Langs.get_text("tutorial_confirm")
                await author.send(tutorial)
                await author.send(tutorial2)
                
            elif p.get_command() == 'help':
                msg = Langs.get_text("tutorial_confirm")
                
                await message.channel.send(msg)
            # Should split on regex with multiple spaces
            parts = message.content.strip().split(' ')
            if len(parts) == 1:
                response = "What " + parts[0] + "??"
            else:
                command = parts[0]
                arg = parts[1]
                CmdInterpreter.interact(command,arg)
            await message.author.send(response)

if __name__ == "__main__":
    Config.load_from('config.json')
    Langs.load_json(Path("res","langs","eng.json"))
    client = MyClient()
    client.run(Config.get_by_key('token'))
