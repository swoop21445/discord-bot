import discord
import re
import secrets
import daemon


def discord_bot():
    client = discord.Client()

    time_relationships = {"GMT":0, "CEST" : 2, "BST" : 1, "EST": -5, "AST":3}

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if "CEST" or "BST" or "EST" or "AST" in message.content:
            try:
                time = re.findall("\d+", message.content)[0]
            except:
                return
            time = int(time)
            if time > 23 and time < 1000:
                return
            zone = re.findall("[A-Z]+", message.content)[0]
            try:
                gmt = time - time_relationships[zone]
            except:
                return
            cest = gmt + time_relationships["CEST"]
            bst = gmt + time_relationships["BST"]
            est = gmt + time_relationships["EST"]
            ast = gmt + time_relationships["AST"]
            time_message = "Central European Summer Time " + str(cest) + "00\n"+"British Summer Time " + str(bst) + "00\n" + "Eastern Standard Time " + str(est) + "00\n" + "Arabian Standard Time " + str(ast) +"00\n"+ "Greenwich Mean Time " + str(gmt) + "00\n"

            await message.channel.send(time_message)

    client.run(secrets.token)

with daemon.DaemonContext():
    discord_bot()