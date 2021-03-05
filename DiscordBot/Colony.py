from random import shuffle, choice
from discord import Game, Embed
from discord.ext import commands
from Token import Colony

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    await bot.change_presence(activity=Game(name="!help"))

@bot.command(name="뽑기")
async def 뽑기(ctx, *args):
    if(len(args) == 0):
        await ctx.send("```!뽑기 [args...]```")
    else:
        await ctx.send(embed=Embed(title="뽑기", description=choice(args)))

@bot.command(name="순서")
async def 순서(ctx, *args):
    if(len(args) == 0):
        await ctx.send("```!순서 [args...]```")
    else:
        args = list(args)
        shuffle(args)
        await ctx.send(embed=Embed(title="순서", description=" - ".join(args)))

@bot.command(name="사다리")
async def 사다리(ctx, *args):
    if(len(args) == 0 or (len(args) % 2) == 1):
        await ctx.send("```!사다리 [args...] [args...]```")
    else:
        a1 = list(args[:len(args) // 2])
        a2 = list(args[len(args) // 2:])
        shuffle(a1)
        shuffle(a2)

        res = []
        for i in range(len(a1)):
            res.append(a1[i])
            res.append(" - ")
            res.append(a2[i])
            res.append("\n")

        await ctx.send(embed=Embed(title="사다리", description="".join(res)))

bot.run(Colony())
