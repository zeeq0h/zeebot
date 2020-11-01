import os
import sys
import asyncio
import random
import discord
from datetime import datetime
from discord.ext import commands

#make the user run as admin


#normal bot stuff
TOKEN = "NzEyNjEyMDA5NTg5MzQyMjE5.XsULDw.V3Ig3ggQsOb-L9CBX3QDWZKMJKU" #outdated token btw


client = commands.Bot(command_prefix = "z!")

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('------')

    #SET A CUSTOM STATUS MESSAGE
    await client.change_presence(activity=discord.Game(name='Getting some upgrades'))


@client.command()
async def ping(ctx):
    print(ctx.author)
    await ctx.send("Pong!")

@client.command()
async def commands(ctx):
    await ctx.send(
"""
z!readme - opens the readme.txt
z!ping - test if the bot is online and responsive
z!clear - clears a specified number of messages
z!dm - dm a specific user in the server
z!anounce - send a dm to every user in the server

""")

@client.command()
async def readme(ctx):
    await ctx.send("""

```
CREATED BY ZEEQOH#1545
ZEE BOT VERSION 0.1 ALPHA
THIS IS NOT A FINISHED PRODUCT SO THERE MAY BE BUGS AND MISSING FEATURES
```

""")

#HOST KILLSWITCH
@client.command()
async def kill(ctx):
    if str(ctx.author) == "zeeqoh#1545":
        await client.close()
    if str(ctx.author) != "zeeqoh#1545":
        await ctx.channel.send("You don't have permission for that!")
        print(ctx.author , " tried to activate the killswitch")

#ADMIN COMMANDS

#clear chat messages
limit = 0
@client.command()
#@commands.has_permissions(administrator=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit = amount + 1)
    await asyncio.sleep(1)
    amount_str = str(amount)
    await ctx.channel.send("Deleted " + amount_str + " messages.")
    await asyncio.sleep(2)
    await ctx.channel.purge(limit = amount ** 0)

#dm a specific user
@client.command()
#@commands.has_permissions(administrator=True)
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await client.fetch_user(user_id)
            await target.send("'" + args + "' *-This is a bot, no replies will be seen or viewed*'")
            await ctx.channel.send("'" + args + "' has been sent to: " + target.name)
            
        except:
            await ctx.channel.send("```An error has occured. please use: z!dm (userID) 'message'``` ")
    else:
        await ctx.channel.send("```An error has occured. please use: z!dm (userID) 'message'``` ")


#dm all users
@client.command()
#@commands.has_permissions(administrator=True)
async def anounce(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' sent to: " + member.name)
            except:
                await ctx.channel.send("```An error has occured. please use: z!dm_all 'message'``` ")
    else:
        await ctx.channel.send("```An error has occured. please use: z!dm_all 'message'```")


#GENERAL USER COMMANDS

client.run(TOKEN)


