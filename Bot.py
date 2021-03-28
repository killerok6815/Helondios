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

@client.command()
async def distcon(ctx, distance, form):
 rv = str(func(distance, form))
 await ctx.send(rv)

def fun(d, f):

    if f.lower() == "ftm":
        rv = int(d) / 3.281

    elif f.lower() == "mft":
        rv = int(d) * 3.281

    elif f.lower() == "mtcm":
        rv = int(d) * 100

    elif f.lower() == "cmmt":
        rv = int(d) / 100

    elif f.lower() == "incm":
        rv = int(d) * 2.54

    elif f.lower() == "cmin":
        rv = int(d) / 2.54

    elif f.lower() == "mk":
        rv = int(d) * 1.609

    elif f.lower() == "km":
        rv = int(d) / 1.609

    elif f.lower() == "yft":
        rv = int(d) * 3

    elif f.lower() == "fty":
        rv = int(d) / 3

    elif f.lower() == "inft":
        rv = int(d) / 12

    elif f.lower() == "ftin":
        rv = int(d) * 12

    else:
        rv = "sorry that measurement doesnt exist."
    return rv


client.run('ODE4NTc1ODAxNTY1MTg0MDAw.YEaEHw.UgQunU01bLvm9Tl4ZoHsGYhtoNE')
