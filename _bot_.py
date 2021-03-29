import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix=['!'])


spam_message = "@everyone"
add_channel_name = "CRAZY"
add_roles_name = "lIIIlllIIllllIIIIlllIIIlIIllII"
bot_token = "Bot Token"


@client.event
async def on_command_error(ctx, error):
    print(error)


@client.command(pass_context=True)
async def spam(ctx, count: int): #run "!spam" to run the command
    await ctx.message.delete()
    for i in range(0, count):
        await ctx.send(spam_message)


@client.command(pass_context=True)
async def add(ctx, count: int):
    await ctx.message.delete()
    guild = ctx.message.guild
    for i in range(0, count):
        await guild.create_text_channel(add_channel_name)


@client.command(pass_context=True)
async def roles(ctx, count: int):
    await ctx.message.delete()
    for i in range(0, count):
        guild = ctx.guild
        await guild.create_role(name=add_roles_name, color=0x8D0000)


client.run(bot_token)