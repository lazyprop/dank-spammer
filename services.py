import asyncio
from main import checkstatus, flipstatus, send_message

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

async def gamble(message,amount, tries,delay = 3):
    if (checkstatus("gamble")):
        await send_message(message,"[.] Already gambling.")
        return

    flipstatus("gamble")
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

async def sellUseless(message):
    if (checkstatus("sell")):
        await send_message("message,Already selling.")
        return
        
    bread = 15
    candy = 12
    chillpill = 11
    cookie = 9

    flipstatus("sell")
    print("[.] Selling all useless items...")
    await send_message(message,"[.] Selling all useless items...")

    while bread:
        await send_message(message,"pls sell bread")
        await asyncio.sleep(3)
        bread-=1
    
    while candy:
        await send_message(message,"pls sell candy")
        await asyncio.sleep(3)
        candy-=1
    
    while chillpill:
        await send_message(message,"pls sell chillpill")
        await asyncio.sleep(3)
        chillpill-=1

    while cookie:
        await send_message(message,"pls sell cookie")
        await asyncio.sleep(3)
        cookie-=1

    await send_message(message,"pls deposit all")
    print("[.] All useless items sold!")