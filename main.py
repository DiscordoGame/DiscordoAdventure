import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!start':
            await message.delete();
            await message.author.send('Hello traveler ' + message.author.name)

client = MyClient()
client.run(open('token.txt', 'r').read())
