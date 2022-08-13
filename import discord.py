import discord
import re


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "CEST" in message.content:
        try:
            time = re.findall("\d+", message.content)[0]
        except:
            return
        print(time)
        time = int(time)
        if time > 23:
            return
        time_message = "British Summer Time " + str(time -1) + "00\n" + "Eastern Standard Time " + str(time - 6) + "00\n" + "Arabian Standard Time " + str(time + 1) +"00"

        await message.channel.send(time_message)

client.run("")