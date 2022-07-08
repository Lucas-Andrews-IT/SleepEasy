# Imports
import discord
from discord import Guild, client, member
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command


# // Core Settings \\ # 

# Place your discord application token here.
BOT_TOKEN: str = "ODc2NjQ2MDkyMTUyOTIyMTEy.YRnGSw.abZdI0deiMi0yUb82uW5oFdNsn0" 

# This is what you could enter before each command in your discord bot.
BOT_PREFIX = "--"

# Allowed bot status online, offline, idle, do_not_disturb, and invisible.
BOT_STATUS = discord.Status.idle

# Brackets will be the bot link for inviting to other
BOT_INVITE = "To add this bot to your own Server, click [invite]"


# // EMBED DEFAULT SETTINGS \\ #

# For all embeded messages to all be the same colour. 
# Example: embed = discord.Embed(title="title name", description="description of embed.", color=config.EMBED_COLOR). 
# Instead of color=0x9b26b9 everytime.
EMBED_COLOR = 0x9b26b9
EMBED_FOOTER = "Task Completed!"


# // Custom Welcome Message + Auto-assign \\ # 

# Server ID and the default role must be placed here
# It's for your 'WELCOME' settings cnofiguration and role that you want auto-assigned (optional)
SERVER_ID = (873238209897844796)
DEFAULT_AUTO_ROLE_ID = (873501999151325205)

# The channel that you want to display the embed message in when new members join.
WELCOME_CHANNEL_ID = (875689116413599845)

# Title and Description of on_member_join event. The variables above can be used like this for a new member joined message.
WELCOME_TITLE = "Member Joined"
WELCOME_DESCRIPTION = "We hope that your time with us is a happy one!" 
# Before this message the start of this description is sent in your server: description=f"{member.mention}, Welcome to {member.guild.name}. "
# can be modifed @ run.py | line 81 | do not remove the 'f' before quotation for user variables.

# Remove the fields that are unused.
WELCOME_FIELD_NAME_1 = "Please check out the Rules Channel!"
WELCOME_FIELD_NAME_2 = "Latest announcements are made here!"

# By copying the ID and placing in between the <> and after the #, It will thus link it in the message so users can click on it;
# users would be redirected to that channel directly instead of searching for it themselves.
WELCOME_FIELD_VALUE_1 = "<#874280280142270504>"
WELCOME_FIELD_VALUE_2 = "<#874280281635438632>"

# Footer message of your Embed
WELCOME_FOOTER = "Task Completed!"


# // Moderation Settings \\ #
STAFF_CHANNEL_REPORT = ()