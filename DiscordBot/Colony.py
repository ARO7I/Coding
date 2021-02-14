from random import shuffle, choice
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
        await ctx.send("!순서 {1} {2} {3}...")
    else:
        arg = list(args)
        random.shuffle(arg)
        await ctx.send(" ".join(arg))

@bot.command(name="뽑기")
async def 뽑기(ctx, *args):
    if(len(args) == 0):
        await ctx.send("!뽑기 {1} {2} {3}...")
    else:
        await ctx.send(random.choice(args))

bot.run(Colony())
