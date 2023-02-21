import discord
import info

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = discord.Client(intents = intents)
    

    @client.event
    async def on_ready():
        print('Logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello')
        
    client.run(info.token)
    
if __name__ == "__main__":
    main()
