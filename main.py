import discord
import asyncio
import time
import json

from services import *

# DISCORD ENV VARS

client = discord.Client()

TOKEN = "NDcyNjU0NzQ0ODgwNjc2ODg5.XoN4tA.htD-Y13LDBKlYgNX2Y-xCQ_cD7Q"
DANKMEMER = "Dank Memer#5192"

@client.event
async def on_message(message):
	splitmsg = message.content.split()

	if (message.author == client.user):

		if (message.content.startswith("//wtf// ")):

			if (splitmsg[1] == "start"):
			
				if (splitmsg[2] == "ezmoney"):
					await send_message(message,"//wtf// start beg")
					await asyncio.sleep(5)
					await send_message(message,"//wtf// start postmeme")
					await asyncio.sleep(5)
					await send_message(message,"//wtf// start deposit")
					await asyncio.sleep(5)
					await send_message(message,"//wtf// start fish")

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

				if (splitmsg[2] == "fish"):
					delay = 30
					if (len(splitmsg) > 3):
						delay = splitmsg[3]
					await fish(message, delay)

				if (splitmsg[2] == "gamble"):
					await gamble(message)

				if (splitmsg[2] == "clear"):
					await clear(message,12,60)

				if (splitmsg[2] == "sell"):
					await sell(message)

				if (splitmsg[2] == "use"):
					await use(message)

			if (splitmsg[1] == "stop"):
				if (len(splitmsg) <= 2):
					return
				if (checkstatus(splitmsg[2])):
					flipstatus(splitmsg[2])

					await send_message(message,"[.] Stopping service {}".format(splitmsg[2]))
					print("[.] Stopping service {}.".format(splitmsg[2]))
	
	# elif str(message.author) == DANKMEMER:
	# 	if (len(message.embeds) > 0): # message has embed
			
	# 		await whichtype(message)

	# 	else:						  # message doesnt have embed
	# 		pass			

def main():
	SENPAI = client.user

	services = ["beg","postmeme","deposit","gamble","use","sell","ezmoney", "fish"]
	try:		
		jsondata = json.loads(open("status.json","r").read())
	except:
		jsondata = dict()

	jsondata["services"] = dict()
	for key in services:
		jsondata["services"][key] = 0

	file = open("status.json","w")
	file.write(json.dumps(jsondata))
	file.close()
	
	print("[.] Welcome Senpai {}".format(SENPAI))
	client.run(TOKEN, bot = False)


if __name__ == '__main__':
	main()
