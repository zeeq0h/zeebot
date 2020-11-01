
import asyncio
import random
import discord
from datetime import datetime
from discord.ext import commands

#make the user run as admin


#normal bot stuff
TOKEN = "NzEyNjEyMDA5NTg5MzQyMjE5.XsUFpg.peeTDHSHSn5uzzKuBEE6wg13XZE"


client = commands.Bot(command_prefix = "z!")

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('------')

    #SET A CUSTOM STATUS MESSAGE
    await client.change_presence(activity=discord.Game(name='Getting some upgrades'))

#Pong message so user can test if bot is responsive
@client.command()
async def ping(ctx):
    print(ctx.author)
    await ctx.send("Pong!")



@client.command()
async def readme(ctx):
    await ctx.send("""

```
CREATED BY ZEEQOH#1545
ZEE BOT VERSION 0.1 ALPHA
THIS IS NOT A FINISHED PRODUCT SO THERE MAY BE BUGS AND MISSING FEATURES
```

""")



client.run(TOKEN)
