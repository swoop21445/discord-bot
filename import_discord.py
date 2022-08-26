import discord
import re
import secrets
"""import daemon"""


def discord_bot():
    client = discord.Client()

    time_relationships = {"GMT":0, "CEST" : 2, "BST" : 1, "CST": -4, "AST":3}

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        message.content = re.sub('<.*?>', '', message.content)
        print(message.content)
        if "Thanks Time bot." in message.content:
            await message.channel.send("https://tenor.com/view/idiocracy-test-genius-iq-gif-14792434")
        if "CEST" or "BST" or "EST" or "AST" in message.content:
            try:
                time = re.findall("\d+", message.content)[0]
            except:
                return
            time = int(time)
            print(time)
            if time > 23 and time < 1000 and time > 2300:
                return

            for timezone in time_relationships.keys():
                search = re.search(timezone,message.content)
                if search:
                    zone = search.group()
            print(zone)
            try:
                gmt = time - time_relationships[zone]
            except:
                return
            cest = gmt + time_relationships["CEST"]
            bst = gmt + time_relationships["BST"]
            cst = gmt + time_relationships["CST"]
            ast = gmt + time_relationships["AST"]
            time_message = "Central European Summer Time " + str(cest) + "00\n"+"British Summer Time " + str(bst) + "00\n" + "Central Standard Time " + str(cst) + "00\n" + "Arabian Standard Time " + str(ast) +"00\n"+ "Greenwich Mean Time " + str(gmt) + "00\n"

            await message.channel.send(time_message)

    client.run(secrets.token)


"""with daemon.DaemonContext():"""
discord_bot()

