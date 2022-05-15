import discord
import random
import asyncio
from discord.ext import commands

HUG = ["https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif", "https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif", "https://c.tenor.com/4n3T2I239q8AAAAC/anime-cute.gif", "https://c.tenor.com/ztEJgrjFe54AAAAC/hug-anime.gif", "https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif", "https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif", "https://c.tenor.com/ItpTQW2UKPYAAAAC/cuddle-hug.gif", "https://c.tenor.com/SXk-WqF6PpQAAAAC/anime-hug.gif", "https://c.tenor.com/X5nBTYuoKpoAAAAC/anime-cheeks.gif", "https://c.tenor.com/SPs0Rpt7HAcAAAAC/chiya-urara.gif", "https://c.tenor.com/mmQyXP3JvKwAAAAC/anime-cute.gif", "https://c.tenor.com/jQ0FcfbsXqIAAAAC/hug-anime.gif", "https://c.tenor.com/z2QaiBZCLCQAAAAC/hug-anime.gif", "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif", "https://c.tenor.com/vkiqyZJWJ4wAAAAC/hug-cat.gif", "https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif", "https://c.tenor.com/nmzZIEFv8nkAAAAC/hug-anime.gif", "https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif", "https://c.tenor.com/WpbZhwwj6zAAAAAC/happy-hug.gif", "https://c.tenor.com/EnfEuWDXthkAAAAC/hug-couple.gif"]
KISS = ["https://c.tenor.com/yoMKK29AMQsAAAAC/kiss-toradora.gif", "https://c.tenor.com/nRdyrvS3qa4AAAAC/anime-kiss.gif", "https://c.tenor.com/-tntwZEqVX4AAAAC/anime-kiss.gif", "https://c.tenor.com/4ofp_xCUBxcAAAAC/eden-of-the-east-akira-takizawa.gif", "https://c.tenor.com/8ln6Z1e-FVYAAAAd/nagumi-koushi-hozumi-serene.gif"]
PUNCH = ["https://c.tenor.com/EvBn8m3xR1cAAAAC/toradora-punch.gif", "https://c.tenor.com/5AsLKQTjbJ4AAAAC/kasumi-love-live.gif", "https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif", "https://c.tenor.com/o8RbiF5-9dYAAAAd/killua-hxh.gif"]

client = discord.Client()
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command()
async def команды(ctx):

    embed = discord.Embed(title="💬Команды бота", description="**Префикс** - .\n\n**Пример** - .команды\n\n**кости** - выдает случайное число от 1 до 100\n**обнять @[имя пользователя]** - обнять упомянутого пользователя\n**цьом @[имя пользователя]** - поцеловать упомянутого пользователя\n**ударить @[имя пользователя]** - ударить упомянутого пользователя\n**очистить [кол-во сообщений для удаления]** - очищает чат на указанное количевство сообщений **(только для админов)**\n**споки @[имя пользователя]** - пожелать спокойной ночи", color = discord.Color.blue())
    await ctx.send(embed=embed)

@client.command()
async def обнять(ctx, member: discord.Member):

    embed = discord.Embed(title="🤗объятия!", description="**{1}** обнял **{0}**!".format(member.name, ctx.message.author.name), color = discord.Color.purple())

    embed.set_image(url = random.choice(HUG))
    await ctx.send(embed=embed)

@client.command()
async def кости(ctx):
    num1 = 1
    num2 = 100
    value = random.randint(num1,num2)
    embed = discord.Embed(title="🎲Случайное число 1-100 для **{0}**".format(ctx.message.author.name), description="Выпало: **{0}**".format(value), color = discord.Color.red())
    await ctx.send(embed=embed)

@client.command()
async def цьом(ctx, member: discord.Member):

    embed = discord.Embed(title="💋поцелуй!", description="**{1}** поцеловал **{0}**!".format(member.name, ctx.message.author.name), color = discord.Color.purple())

    embed.set_image(url = random.choice(KISS))
    await ctx.send(embed=embed)

@client.command()
async def ударить(ctx, member: discord.Member):

    embed = discord.Embed(title="👊удар!", description="**{1}** ударил **{0}**!".format(member.name, ctx.message.author.name), color = discord.Color.red())

    embed.set_image(url = random.choice(PUNCH))
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def очистить(ctx, arg):
    embed = discord.Embed(title="🧹Чат очищен".format(ctx.message.author.name), description="Удалено {0} сообщений".format(arg), color = discord.Color.green())
    await ctx.channel.purge(limit=int(arg))
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

@client.command()
async def споки(ctx, member: discord.Member):

    embed = discord.Embed(title="🌙", description="**{1}** пожелал спокойной ночи **{0}**!".format(member.name, ctx.message.author.name), color = discord.Color.blue())

    await ctx.send(embed=embed)

client.run('OTc1MDAwNDQ0MzQ0NjAyNjY0.GoJ62C.Yk0T7SyBO7gH2EO7Qash2MPI-vWrk3hXp1hvDQ')