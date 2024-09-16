# client id 805459804059467796
# permission n. 67584

import discord
from discord.ext import commands
import asyncio
import datetime

bot = commands.Bot(command_prefix="pls ")


@bot.event
async def on_ready():
    print(f"{bot.user.name} is online and ready.")

snipe_author = None
snipe_content = None
snipe_id = None

edit_author = None
edit_content = None
edit_id = None


@bot.event
async def on_message_delete(message):
    global snipe_content
    global snipe_author
    global snipe_id

    snipe_content = message.content
    snipe_author = message.author
    snipe_id = message.id

    await asyncio.sleep(60)

    if message.id == snipe_id:
        snipe_author = None
        snipe_content = None
        snipe_id = None


@bot.event
async def on_message_edit(m_before, m_after):
    global edit_author
    global edit_content
    global edit_id

    edit_author = m_before.author
    edit_content = m_before.content
    edit_id = m_before.id

    await asyncio.sleep(60)

    if m_before.id == edit_id:
        edit_author = None
        edit_content = None
        edit_id = None


@bot.command(name='snipe')
async def snipe(ctx):
    try:
        em = discord.Embed(description=snipe_content,
                           color=discord.Color.purple(), timestamp=datetime.datetime.utcnow())
        em.set_author(name=snipe_author, icon_url=snipe_author.avatar_url)
        await ctx.send(embed=em)
    except:
        await ctx.send("There's nothing to snipe!")


@bot.command(name="esnipe")
async def esnipe(ctx):
    try:
        emb = discord.Embed(description=edit_content,
                            color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
        emb.set_author(name=edit_author, icon_url=edit_author.avatar_url)
        await ctx.send(embed=emb)
    except:
        await ctx.send("There's nothing to snipe!")


bot.run("PK") #PK = Private Key
