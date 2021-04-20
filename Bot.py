import datetime
import pytz
import discord
from discord.ext import commands

#~~~~~~~~~~~~~~~~~INITIALIZATION~~~~~~~~~~~~~~~~~

client = commands.Bot(command_prefix = ['kilu ', 'kilu', 'Kilu ', 'Kilu', 'k.')

#~~~~~~~~~~~~~~~~~~~~~EVENTS~~~~~~~~~~~~~~~~~~~~~~~

@client.event
async def on_ready():
    print("online")

#~~~~~~~~~~~~~~~~~~~~COMMANDS~~~~~~~~~~~~~~~~~~~~~~~

client.remove_command('help')

#HELP

@client.command(aliases = ["help", "cmd", "commands", "cmds])
async def help(ctx):

    with open("cmd_help.txt") as f:
        dat = f.readlines()

    cmd_str = ""

    for i in dat:
        cmd_str += i

    embed=discord.Embed(title="Command Help", color=0x8f0921)
    embed.add_field(name="General List", value=cmd_str, inline=False)
    await ctx.send(embed=embed)

#MISC

@client.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

#CONVERSIONS
#----- Distance:

@client.command(aliases=["ftm", "fm", "f2m"])
async def feet_to_metre(ctx, dist):
    dv = int(dist) / 3.281
    await ctx.send(dv)

@client.command(aliases=["mft", "mtf", "mf", "m2f"])
async def metre_to_feet(ctx, dist):
    dv = int(dist) * 3.281
    await ctx.send(dv)

@client.command(aliases=["mtcm", "mcm", "m2c"])
async def metre_to_centimetre(ctx, dist):
    dv = int(dist) * 100
    await ctx.send(dv)

@client.command(aliases=["ctm", "c2m", "cmm"])
async def centimetre_to_metre(ctx, dist):
    dv = int(dist) / 100
    await ctx.send(dv)

@client.command(aliases=["intcm", "incm", "i2c"])
async def inch_to_centimetre(ctx, dist):
    dv = int(dist) * 2.54
    await ctx.send(dv)

@client.command(aliases=["cmtin", "cmin", "c2i"])
async def centimetre_to_inch(ctx, dist):
    dv = int(dist) / 2.54
    await ctx.send(dv)

@client.command(aliases=["mtk", "mk", "m2k"])
async def mile_to_kilometre(ctx, dist):
    dv = int(dist) * 1.609
    await ctx.send(dv)

@client.command(aliases=["ktm", "km", "k2m"])
async def kilometre_to_mile(ctx, dist):
    dv = int(dist) / 1.609
    await ctx.send(dv)

@client.command(aliases=["ytft", "ytf", "yft", "y2f"])
async def yard_to_feet(ctx, dist):
    dv = int(dist) * 3
    await ctx.send(dv)

@client.command(aliases=["fty", "fy", "f2y"])
async def feet_to_yard(ctx, dist):
    dv = int(dist) / 3
    await ctx.send(dv)

@client.command(aliases=["inft", "ift", "i2f"])
async def inch_to_feet(ctx, dist):
    dv = int(dist) / 12
    await ctx.send(dv)

@client.command(aliases=["ftin", "fti", "f2i"])
async def feet_to_inch(ctx, dist):
    dv = int(dist) * 12
    await ctx.send(dv)

#----- Mass:

@client.command(aliases=["lbkg", "l2k"])
async def pound_to_kilos(ctx, weight):
    m = int(weight) / 2.20462262
    await ctx.send(m)

@client.command(aliases=["kglb", "k2l"])
async def kilos_to_pounds(ctx, weight):
    m = int(weight) * 2.20462262
    await ctx.send(m)

@client.command(aliases=["gkg", "g2k"])
async def grams_to_kilos(ctx, weight):
    m = int(weight) / 1000
    await ctx.send(m)


@client.command(aliases=["kgg", "k2g"])
async def kilos_to_grams(ctx, weight):
    m = int(weight) * 1000
    await ctx.send(m)

@client.command(aliases=["ozkg", "o2k"])
async def ounces_to_kilos(ctx, weight):
    m = int(weight) / 35.273962
    await ctx.send(m)

@client.command(aliases=["kgoz", "k2o"])
async def kilos_to_ounces(ctx, weight):
    m = int(weight) * 35.273962
    await ctx.send(m)

#----- Temperature:

@client.command(aliases=["ftc", "fc", "f2c"])
async def fahrenheit_to_celsius(ctx, temp=0):
    rv = (int(t)- 32.0) * 5.0 / 9.0
    await ctx.send(rv)

@client.command(aliases=["ctf", "cf", "c2f"])
async def celsius_to_fahrenheit(ctx, temp=0):
    rv = (int(t)* 9.0 / 5.0) + 32.0
    await ctx.send(rv)

@client.command(aliases=["ftk", "fk", "f2k"])
async def fahrenheit_to_kelvin(ctx, temp=0):
    rv = (int(t)- 32.0) * 5.0 / 9.0 + 273.15
    await ctx.send(rv)

@client.command(aliases=["ctk", "ck", "c2k"])
async def celsius_to_kelvin(ctx, temp=0):
    rv = int(t) + 273.15
    await ctx.send(rv)

@client.command(aliases=["ktf", "kf", "k2f"])
async def kelvin_to_fahrenheit(ctx, temp=0):
    rv = ((int(t) -273.15)- 32.0) * 5.0 / 9.0
    await ctx.send(rv)

@client.command(aliases=["ktc", "kc", "k2c"])
async def kelvin_to_celsius(ctx, temp=0):
    rv = int(t) - 273.15
    await ctx.send(rv)

#MATH COMMANDS

@client.command(aliases=["math", "calc", "op", "add", "subtract", "sub", "multiply", "mul", "divide", "div", "mod"])
async def basic_calculation(ctx, *, expression):
    expression = expression.split(' ')
    expl = [x for x in expression]
    while ' ' in expl:
        expl.remove(' ')
    a, o, b = expl[0], expl[1], expl[2]
    str_ex = a + o + b
    sum = eval(str_ex)
    await ctx.send(sum)

#~~~~~~~~~~~~~~~~~~~~~~~RUN~~~~~~~~~~~~~~~~~~~~~~~~~

client.run('ODE4NTc1ODAxNTY1MTg0MDAw.YEaEHw.UgQunU01bLvm9Tl4ZoHsGYhtoNE')
