import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # We only accept messages from TextChannels
        if isinstance(message.content, discord.TextChannel) and message.content == '!start':
            # Delete the message that the user sent with '!start' in the general channel
            await message.delete();
            # DM the author of message with a greating
            await message.author.send('Hello traveler ' + message.author.name + ".")

client = MyClient()
client.run(open('token.txt', 'r').read())
