import discord
import info

from random import randint

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = discord.Client(intents = intents)
    

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello')
            
    #Simple command, it basicaly returns a string from a array and send in the channel        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.startswith('$citacao'):
            await message.channel.send(info.citacoes[randint(0,5)])
        
    client.run(info.token)
    
if __name__ == "__main__":
    main()
