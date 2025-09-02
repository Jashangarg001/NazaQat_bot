import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import json
from datetime import timedelta

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="//", intents=intents, case_insensitive=True)
#
# AFK_FILE = "afk_users.json"
#
# # Load AFK users from file if it exists
# afk_users = {}
# if os.path.exists(AFK_FILE) and os.path.getsize(AFK_FILE) > 0:
#     with open(AFK_FILE, "r") as read_file:
#         afk_users = json.load(read_file)
#
#
# def save_afk():
#     """Save AFK users to file"""
#     with open(AFK_FILE, "w") as write_file:
#         json.dump(afk_users, write_file)
#
#
# @bot.event
# async def on_ready():
#     print(f"Logged in as {bot.user}")
#
# @bot.command()
# async def afk(ctx, *, reason="AFK"):
#     afk_users[str(ctx.author.id)] = reason
#     save_afk()
#     await ctx.send(f"{ctx.author.mention} is now AFK : {reason}")
#
# @bot.event()
# async def back(ctx):
#     if str(ctx.author.id) in afk_users:
#         del afk_users[str(ctx.author.id)]
#         save_afk()
#         await ctx.send(f"Welcome back {ctx.author.mention}!")
#     else:
#         await ctx.send("You were not marked as AFK.")
#     if message.author.id in afk_users:
#         del afk_users[message.author.id]
#         await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK status.")
#
#     if message.mentions:
#         for user in message.mentions:
#             if user.id in afk_users:
#                 reason = afk_users[user.id]
#                 await message.channel.send(f"{user.display_name} is AFK: {reason}")
#
#     await bot.process_commands(message)

# Command to set AFK
# @bot.command()
# async def afk(ctx, *, reason="AFK"):
#     afk_users[str(ctx.author.id)] = reason
#     save_afk()
#     await ctx.send(f"{ctx.author.mention} is now AFK: {reason}")


# Command to remove AFK
# @bot.command()
# async def back(ctx):
#     if str(ctx.author.id) in afk_users:
#         del afk_users[str(ctx.author.id)]
#         save_afk()
#         await ctx.send(f"Welcome back {ctx.author.mention}!")
#     else:
#         await ctx.send("You were not marked as AFK.")
#     if message.author.id in afk_users:
#         del afk_users[message.author.id]
#         await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK status.")

# # When someone mentions an AFK user
# @bot.event
# async def on_message(message):
#     if message.author.bot:
#         return
#
#     for user in message.mentions:
#         if str(user.id) in afk_users:
#             await message.channel.send(f"{user.name} is AFK: {afk_users[str(user.id)]}")
#
#     await bot.process_commands(message)

# #AFK COMMAND
#
# @bot.event
# async def on_ready():
#     print(f"✅ Logged in as {bot.user}")
#
# @bot.command()
# async def afk(ctx, *, reason="AFK"):
#     afk_users[ctx.author.id] = reason
#     await ctx.send(f"{ctx.author.mention} is now AFK : {reason}")
#
# @bot.event
# async def on_message(message):
#     if message.author.bot:
#         return
#
#     if message.author.id in afk_users:
#         del afk_users[message.author.id]
#         await message.channel.send(f"Welcome back {message.author.mention}, I removed your AFK status.")
#
#     if message.mentions:
#         for user in message.mentions:
#             if user.id in afk_users:
#                 reason = afk_users[user.id]
#                 await message.channel.send(f"{user.display_name} is AFK: {reason}")
#
#     await bot.process_commands(message)
#AVATAR COMMAND

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

@bot.command(name="avatar")
@commands.has_permissions(administrator=True)
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    avatar_url = member.display_avatar.url
    embed = discord.Embed(title=f"{member}'s Avatar", color=discord.Color.blue())
    embed.set_image(url=avatar_url)
    await ctx.send(embed=embed)
# #WARN, BAN, TIMEOUT, KICK COMMAND
#
# warnings = {}
#
# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user}')
#
# @bot.command()
# @commands.has_permissions(administrator=True)
# async def warn(ctx, member: discord.Member, *, reason="No reason provided"):
#     if member.bot:
#         return await ctx.send("You can't warn bots.")
#
#     if member == ctx.author:
#         return await ctx.send("You can't warn yourself.")
#
#     user_id = str(member.id)
#     if user_id not in warnings:
#         warnings[user_id] = []
#
#     warnings[user_id].append(reason)
#
#     await ctx.send(f"{member.mention} has been warned. Reason: {reason} "
#                    f"(Total warnings: {len(warnings[user_id])})")
#
#     try:
#         await member.send(f"You have been warned in **{ctx.guild.name}**.\n"
#                           f"Reason: {reason}\n"
#                           f"Total warnings: {len(warnings[user_id])}")
#     except discord.Forbidden:
#         await ctx.send(f"Couldn't send a Warning DM to {member.mention}.")
#
# @bot.command()
# @commands.has_permissions(administrator=True)
# async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
#     await member.kick(reason=reason)
#     await ctx.send(f"{member.mention} has been kicked. Reason: {reason}")
#
#     try:
#         await member.send(f"You have been kicked from **{ctx.guild.name}**.\n"
#                           f"Reason: {reason}\n")
#
#     except discord.Forbidden:
#         await ctx.send(f"Couldn't send a Kick DM to {member.mention}.")
#
# @bot.command()
# @commands.has_permissions(administrator=True)
# async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
#     await member.ban(reason=reason)
#     await ctx.send(f"{member.mention} has been banned. Reason: {reason}")
#
#     try:
#         await member.send(f"You have been Banned from **{ctx.guild.name}**.\n"
#                           f"Reason: {reason}\n")
#
#     except discord.Forbidden:
#         await ctx.send(f"Couldn't send a Ban DM to {member.mention}.")
#
# @bot.command()
# @commands.has_permissions(administrator=True)
# async def timeout(ctx, member: discord.Member, seconds: int, *, reason="No reason provided"):
#     try:
#         duration = timedelta(seconds=seconds)
#         until_time = discord.utils.utcnow() + duration
#         await member.timeout(until_time, reason=reason)
#         await ctx.send(f"{member.mention} has been timed out for {seconds} seconds. Reason: {reason}")
#     except Exception as e:
#         await ctx.send(f"Could not timeout: {e}")
#
#     try:
#         await member.send(f"You have been given timeout in **{ctx.guild.name}**.\n"
#                           f"Reason: {reason}\n"
#                           f"For {seconds} seconds.\n")
#     except discord.Forbidden:
#         await ctx.send(f"Couldn't send a Timeout DM to {member.mention}.")
#
# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You don't have permission to use this command.")
#     elif isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Missing argument. Check the command usage.")
#     elif isinstance(error, commands.MemberNotFound):
#         await ctx.send("User not found.")
#     else:
#         await ctx.send(f"An error occurred: {str(error)}")
#BOT STATUS

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Activity(type=discord.ActivityType.listening, name="Ayakashki 💖"))

bot.run(TOKEN)
