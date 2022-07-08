# https://github.com/SleepySlothx/SleepEasyBOT

# Imports
import time
import json
import discord
import os
from cogwatch import Watcher
from colorama import Fore
from colorama.ansi import Fore
from discord import member
from discord.ext import commands

# Importing the preset configuration from config.py
from configuration import config

intents = discord.Intents.default()
intents.members = True
intents = intents.all()

# Settings of discord.bot as client and the removal of in-built 'help'
client = commands.Bot(command_prefix=config.BOT_PREFIX, help_command=None, intents=intents) # Change prefix as you please!
client.remove_command("help") # Custom help command modifications can be made in /commands/commandlist.py


@client.event
async def on_ready():
    
    # Instantly reloads all cogs and updates to current saved version without restarting.
    watcher1 = Watcher(client, path='commands', preload=True)

    # Starts the watcher to look for changes in cogs for folder 'commands'
    await watcher1.start()

    
    # License used for SleepEasy
    print(" ")
    print("License")
    print(" ")
    print("Copyright (C) 2021 SleepySlothx")
    print(" ")
    print("This program is free software: you can redistribute it and/or modify")
    print("it under the terms of the GNU General Public License as published by")
    print("the Free Software Foundation, either version 3 of the License, or")
    print("(at your option) any later version.\n")
    print("This program is distributed in the hope that it will be useful,")
    print("but WITHOUT ANY WARRANTY; without even the implied warranty of")
    print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the")
    print("GNU General Public License for more details.")
    print("<http://www.gnu.org/licenses/>\n\n")
    print("GitHub: Lucas-Andrews-IT")
    print("Discord: SleepySloth#0001")
    print("E-mail: lucasandrews.it@gmail.com\n")

    # Checking if a bot token has been set.
    if config.BOT_TOKEN == "":
        print("Error: No application token detected!")
        exit

    else:
        
        # Prints the name of the discord bot.
        print(Fore.RED + "Application logged in as:", Fore.RESET + client.user.name)
        print(Fore.RESET + "\n")

        await client.change_presence(status=config.BOT_STATUS, activity=discord.Activity(type=discord.ActivityType.watching, name="for {}help".format(config.BOT_PREFIX)))
        
        # Displaying all current servers the bot is currently residing in.
        print("Currently loaded in:" + Fore.YELLOW)
        for guild in client.guilds:
            print (guild.name)
    
    # Resets colour back to white instead of yellow.
    print (Fore.RESET)

@client.event
async def on_member_join(member): # Only 1 parameter for on_member_join
        
        # Checking if the ID matches the one set for your discord server to do the following actions after.
        if member.guild.id == config.SERVER_ID:

            # Getting the role from the configuration.
            role = discord.utils.get(member.guild.roles, id=config.DEFAULT_AUTO_ROLE_ID)

            # Where the configuration of your Welcome message title and description will be placed.
            # mention user | {member.mention}
            # mention server name | {member.guild.name}
            embed = discord.Embed(title=(config.WELCOME_TITLE), description=f"{member.mention}, Welcome to {member.guild.name }. " + config.WELCOME_DESCRIPTION, color=config.EMBED_COLOR, font_size=200)

            # Where the configuration of your set fields of the name chosen and value/message are placed.
            embed.add_field(name=config.WELCOME_FIELD_NAME_1, value=config.WELCOME_FIELD_VALUE_1, inline=False)
            embed.add_field(name=config.WELCOME_FIELD_NAME_2, value=config.WELCOME_FIELD_VALUE_2, inline=False)
            embed.set_footer(text=config.WELCOME_FOOTER)
            
            # Send the embed message and fields
            # Welcome Channel ID will be set here and sends the embed to that channel ID. 
            await client.get_channel(config.WELCOME_CHANNEL_ID).send(embed=embed)

            # Get role and assign to new member, when they join your discord server.
            await member.add_roles(role)
            
        else:
            return
        

        # This writes to a file the time and date a user has joined a specific server with an apendage.
        a = (f"{member} has joined {member.guild.name}. ")
        t = time.localtime()
        date = time.strftime("%Y-%m-%d")
        current_time = time.strftime("%H:%M:%S", t)
        a = a + (f"{date} at {current_time}")
        with open("logs/join.txt", "a") as f:
            f.write(a + "\n")

        # The folder we want to generate the file in with the guild name intact.
        dir = (f"./logs/")
        dir = dir + (f"{member.guild.name}/") # Append the guild name to the folder.
        dir = dir + (f"{date}/") # Append the date to the folder.
        dir = dir + (f"{current_time}/") # Append the time to the folder.
        dir = dir + (f"{member}/") # Append the user to the folder.
        dir = dir + (f"{member.guild.name}-{member.guild.id}-{member.id}-{member.name}-{member.discriminator}.txt") # Append the file name to the folder.


        # Creates the folder if it doesn't exist.
        if not os.path.exists(dir):
            os.makedirs(dir)
            

        # It will write to the selected directory, './logs/', with the guild name and the action. It will include the time and date variables aswell.
        with open((dir) + f"{member.guild.name}_members_joined.txt", 'a') as f:
            f.write(a + "Time/Date: " + current_time + " " + date + "\n")


@client.event
async def on_member_remove(member):

    # Writes to a file the time and date a user has left a specific server with an appendage.
    a = (f"{member} has left {member.guild.name}. ")
    t = time.localtime()
    date = time.strftime("%Y-%m-%d")
    current_time = time.strftime("%H:%M:%S", t)

    # Folder we want to generate the file in with the guild name intact.
    dir = (f"./logs/")
    dir = dir + (f"{member.guild.name}-{member.guild.id}-{member.id}-{member.name}-{member.discriminator}.txt") # Append the file name to the folder.

    # Writes to the selected directory, './logs/', with the guild name and the action. It will include the time and date variables aswell.
    with open((dir) + f"{member.guild.name}_members_left.txt", 'a') as f:
        f.write(a + "Time/Date: " + current_time + " " + date + "\n")

        if member.guild.id == config.SERVER_ID:
            # Get role and remove from member, when they leave your discord server.
            role = discord.utils.get(member.guild.roles, id=config.DEFAULT_AUTO_ROLE_ID)
            await member.remove_roles(role)
        else:
            return



@client.event
async def on_guild_join(guild):
    
    # Writes to a file the time and date a user has left a specific server with an appendage.
    a = (f"{client.user.name} has joined '{guild.name}' : '{guild.id}'. ")
    t = time.localtime()
    date = time.strftime("%Y-%m-%d")
    current_time = time.strftime("%H:%M:%S", t)

    # Folder we want to generate the file in with the guild name intact.
    dir = (f"./logs/")

    # Writes to the selected directory, './logs/', with the guild name and the action. It will include the time and date variables aswell.
    with open((dir) + f"bot_joined.txt", 'a') as f:
        f.write(a + "Time/Date: " +current_time + " " + date + "\n")

        if guild.id == config.SERVER_ID:
            # Get role and assign to new member, when they join your discord server.
            role = discord.utils.get(guild.roles, id=config.DEFAULT_AUTO_ROLE_ID)
            await guild.owner.add_roles(role)

@client.event
async def on_guild_remove(guild):
    
    # Writes to a file the time and date a user has left a specific server with an appendage.
    a = (f"{client.user.name} was removed from '{guild.name}' : '{guild.id}'. ")
    t = time.localtime()
    date = time.strftime("%Y-%m-%d")
    current_time = time.strftime("%H:%M:%S", t)

    # Folder we want to generate the file in with the guild name intact.
    dir = (f"./logs/")

    # Writes to the selected directory, './logs/', with the guild name and the action. It will include the time and date variables aswell.
    with open((dir) + f"bot_removed.txt", 'a') as f:
        f.write(a + "Time/Date: " + current_time + " " + date + "\n")


# Run bot
client.run(config.BOT_TOKEN)