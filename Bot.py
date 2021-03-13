import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'kilu ')

@client.event
async def on_ready():
    print("online")

@client.command()
async def conv(ctx, temp, form):
 rv = str(func(temp, form))
 await ctx.send(rv)

def func(t, f):
    if t == 0 and f.lower() == "f":
        rv = "-17.8"

    elif f.lower() == "f":
        rv = (int(t)- 32) * 5 / 9

    elif f.lower() == "c":
     rv = (int(t)* 9 / 5) + 32

    elif f.lower() == "fk":
     rv = (int(t)- 32) * 5 / 9 + 273.15

    elif f.lower() == "ck":
     rv = int(t)+ 273.15

    else:
     rv = "sorry that measurement doesnt exist."
    return rv

@client.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

@client.command()
async def cmds(ctx):
    embed=discord.Embed(title="Command Help", color=0x8f0921)
    embed.add_field(name="General list (wip)", value="cmds\n\nconv (*number*) (*measurement)* to convert from: c, f, ck, fk\n\nsay (msg here)", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def div (ctx, a, b):
    a, b = int(a), int(b)
    q = a / b
    r = a % b
    li = "-----"

    for i in str(a):
        li += "--"

    await ctx.send(f"     {q}")
    await ctx.send(li)
    await ctx.send(f"{b} | {a} ")
    await ctx.send(li)
    await ctx.send(f"    {r} ")

client.run('ODE4NTc1ODAxNTY1MTg0MDAw.YEaEHw.UgQunU01bLvm9Tl4ZoHsGYhtoNE')
