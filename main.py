import discord
import asyncio
import time
import json

from services import *
# DISCORD ENV VARS

info = json.loads(open("info.json","r").read())

TOKEN = info["token"]
SENPAI = info["username"]
SENPAI_ID = info["userid"]

client = discord.Client()

def checkstatus(name):
    stringdata = open("status.json","r").read()
    jsondata = json.loads(str(stringdata))
    # print(stringdata)
    return jsondata["services"][name]
    # return

def flipstatus(name):
    jsondata = json.loads(open("status.json","r").read())
    jsondata["services"][name]^= 1

    file = open("status.json","w")
    file.write(json.dumps(jsondata))
    file.close()

@client.event
async def on_message(message):
    splitmsg = message.content.split()
    # print(splitmsg)

    if (message.content.startswith("wtf")):
        if (str(message.author) == SENPAI):

            if (splitmsg[1] == "start"):
            
                if (splitmsg[2] == "ezmoney"):
                    await send_message(message,"wtf start beg")
                    await asyncio.sleep(3)
                    await send_message(message,"wtf start postmeme")
                    await asyncio.sleep(3)
                    await send_message(message,"wtf start deposit")

                if (splitmsg[2] == "beg"):
                    delay = 30
                    if (len(splitmsg) > 3):
                        delay = int(splitmsg[3])
                    await beg(message,delay)

                if (splitmsg[2] == "deposit"):
                    delay = 30
                    if (len(splitmsg) > 3):
                        delay = int(splitmsg[3])
                    await deposit(message,delay)

                if (splitmsg[2] == "postmeme"):
                    delay = 60
                    if (len(splitmsg) > 3):
                        delay = splitmsg[3]
                    await postmeme(message, delay)

                if (splitmsg[2] == "gamble"):
                    delay = 3
                    if (len(splitmsg) > 3):
                        delay = int(splitmsg[3])
                        await postmeme(message,delay)

                    amount = int(splitmsg[3])
                    tries = int(splitmsg[4])
                    await gamble(message,amount,tries)

                if (splitmsg[2] == "clear"):
                    await clear(message,12,60)

                if (splitmsg[2] == "sell"):
                    await sellUseless(message)

            if (splitmsg[1] == "stop"):
                if (len(splitmsg) <= 2):
                    return
                if (checkstatus(splitmsg[2])):
                    flipstatus(splitmsg[2])

                    await send_message(message,"[.] Stopping service {}".format(splitmsg[2]))
                    print("[.] Stopping service {}.".format(splitmsg[2]))

        else:
            await send_message(message,"[.] Sorry <@{}>, I only answer to Senpai <@{}>".format(
                message.author.id,SENPAI_ID
            )) 
    
async def send_message(message,content,clear=False):
    await message.channel.send(content)
    if (clear):
        await message.channel.send("pls clear")


def main():
    
    jsondata = json.loads(open("status.json","r").read())
    for key in jsondata["services"].keys():
        jsondata["services"][key] = 0

    file = open("status.json","w")
    file.write(json.dumps(jsondata))
    file.close()
    
    print("[.] Welcome Senpai {}".format(SENPAI))
    client.run(TOKEN, bot = False)


if __name__ == '__main__':
    main()