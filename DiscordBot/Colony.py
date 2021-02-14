from random import shuffle, choice
from discord import Embed
from discord.ext import commands
from Token import Colony

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

@bot.command(name="순서")
async def 순서(ctx, *args):
    if(len(args) == 0):
        await ctx.send("```!순서 [args...]```")
    else:
        args = list(args)
        shuffle(args)
        await ctx.send(embed = Embed(title="순서", description=" - ".join(args)))

@bot.command(name="뽑기")
async def 뽑기(ctx, *args):
    if(len(args) == 0):
        await ctx.send("```!뽑기 [args...]```")
    else:
        await ctx.send(embed = Embed(title="뽑기", description=choice(args)))

bot.run(Colony())
