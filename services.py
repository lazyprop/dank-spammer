import asyncio
import json

async def beg(message,delay = 30):
    if (checkstatus("beg")):
        await send_message(message,"[.] Already begging.")
        return

    flipstatus("beg")
    print("[.] Begging after every {} seconds...".format(delay))
    await send_message(message,"[.] Begging after every {} seconds...".format(delay))
    while checkstatus("beg"):
        await send_message(message,"pls beg")
        await asyncio.sleep(delay)

async def deposit(message,delay = 30):
    if (checkstatus("deposit")):
        await send_message(message,"[.] Already depositing.")
        return

    flipstatus("deposit")
    print("[.] Depositing after every {} seconds...".format(delay))
    await send_message(message,"[.] Depositing after every {} seconds...".format(delay))
    while checkstatus("deposit"):
        await send_message(message,"pls deposit all")
        await asyncio.sleep(delay)

async def postmeme(message, delay = 60):
    if (checkstatus("postmeme")):
        await send_message(message,"[.] Already posting memes.")
        return

    flipstatus("postmeme")
    print("[.] Posting memes after every {} seconds...".format(delay))
    await send_message(message,"[.] Posting memes after every {} seconds...".format(delay))
    while checkstatus("postmeme"):
        for x in "nerd":
            await send_message(message,"pls postmeme")
            await send_message(message,x)
            await asyncio.sleep(delay)

async def gamble(message,delay = 3):
    if (checkstatus("gamble")):
        await send_message(message,"[.] Already gambling.")
        return

    flipstatus("gamble")

    args = message.content[3:].split()
    amount = args[0].split(":")[0]


    print("[.] Gambling with {} coins a total of {} times...".format(amount, tries))
    await send_message(message,"[.] Gambling with {} coins a total of {} times...".format(amount, tries))
    count = 0

    while count < tries and checkstatus("gamble"):
            await send_message(message,"pls withdraw {}".format(amount))
            await asyncio.sleep(delay)
            await send_message(message,"pls gamble {}".format(amount))
            await asyncio.sleep(delay)
            await send_message(message,"pls deposit all")
            await asyncio.sleep(delay)
            count+=1

    print("[.] Gambling {} times completed!".format(tries))
    await send_message(message,"[.] Gambling {} times completed!".format(tries))

async def clear(message,num,delay):
    print("[.] Clearing {} messages every {} seconds...".format(num,delay))
    await send_message(message,"[.] Clearing {} messages every {} seconds...".format(num,delay))

    flipstatus("clear")
    while checkstatus("clear"):
        await send_message(message,"pls clear {}".format(num))
        await asyncio.sleep(delay)

async def sell(message,delay=4):
    if (checkstatus("sell")):
        await send_message(message,"[.] Already selling.")
        return        
    
    flipstatus("sell")
    print("[.] Selling...")
    await send_message(message,"[.] Selling...")

    for item in message.content.split()[3:]:
        it = item.split(':')[0]
        val = int(item.split(':')[1])

        await send_message(message,"[>] Selling {} {}s...".format(val,it))

        count = 0
        while count < val:
            await send_message(message, "pls sell {}".format(it))
            count+= 1
            await asyncio.sleep(delay)

        await send_message(message, "[>] Sold {} {}s.".format(val,it))

    print("[.] All items sold!")
    await send_message(message,"[.] All items sold!")

async def use(message,delay=5   ):
    if (checkstatus("use")):
        await send_message(message,"[.] Already using.")
        return        
    
    flipstatus("use")

    print("[.] Using...")
    await send_message(message,"[.] Using...")

    for item in message.content.split()[3:]:
        it = item.split(':')[0]
        val = int(item.split(':')[1])

        await send_message(message,"[>] Using {} {} times...".format(it,val))

        count = 0
        while count < val:
            await send_message(message, "pls use {}".format(it))
            count+= 1
            await asyncio.sleep(delay)

        await send_message(message, "[>] Used {} {} times.".format(it,val))

    flipstatus("use")
    print("[.] All items used!")
    await send_message(message,"[.] All items used!")

async def send_message(message,content,clear=False):
    await message.channel.send(content)
    if (clear):
        await message.channel.send("pls clear")

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