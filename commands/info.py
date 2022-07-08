# https://github.com/SleepySlothx/SleepEasyBOT

# Imports
import sys
import traceback
import time
import json
import discord
from discord.ext import commands
from discord.ext.commands.core import command

# Importing the preset configuration from config.py
from configuration import config


class info(commands.Cog):
    def __init__(self, client):
        self.client = client


# Server Info Command
    @commands.command(aliases = ['botinfo'])
    async def info(self, ctx):
        await ctx.send(f"info was here.")
        return


# Poll Command from StackOverFlow on the 7/08/2021 @ 1:21AM
    @commands.command(pass_context=True, aliases = ['vote'])
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, question, option1=None, option2=None):

        if option1==None and option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**")
            await message.add_reaction('✅')
            await message.add_reaction('❎')
        
        elif option1==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = No**")
            await message.add_reaction('✅')
            await message.add_reaction('❎')
        
        elif option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = {option2}**")
            await message.add_reaction('✅')
            await message.add_reaction('❎')
        
        else:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = {option2}**")
            await message.add_reaction('✅')
            await message.add_reaction('❎')

# Discord bot invite to other servers.
    @commands.command(aliases = ['addbot', 'invitebot'])
    async def invite(self, ctx):
    
        # Writes to a file the time and date a user has left a specific server with an appendage.
        a = (f"{ctx.message.author} wants to invite your bot to their server. ")
        t = time.localtime()
        date = time.strftime("%Y-%m-%d")
        current_time = time.strftime("%H:%M:%S", t)

        # Folder we want to generate the file in with the guild name intact.
        dir = (f"/logs")

        # Writes to the selected directory, './logs/', with the guild name and the action. It will include the time and date variables aswell.
        with open((dir) + f"bot_invites.txt", 'a') as f:
            f.write(a + current_time + " " + date + "\n")
    
        async with ctx.channel.typing():
            # This will create an embed that will allow you to invite the bot to other discod servers.
            embed = discord.Embed(title="Invite", description=config.BOT_INVITE + "(https://discordapp.com/oauth2/authorize?client_id={}&scope=bot>)".format(self.client.user.id), color=config.EMBED_COLOR)
            embed.set_footer(text=f"Requested by {ctx.message.author}")
    
            # Sends the 'embed' to the user
            await ctx.send(embed=embed)
            return

# Report member to Staff Chat
    @commands.command(aliase=['rep'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def report(self, ctx, user : discord.Member, * reason):

            channel = self.client.get_channel(config.STAFF_CHANNEL_REPORT) # Staff Channel Here
            author = ctx.message.author
            rearray = ' '.join(reason[:]) # Converts reason argument array to string
        
            if not rearray: # If no reason specific
                await channel.send(f"{author} has reported {user}, Reason: Not provided.")
                await ctx.message.delete() # Remove last message
        
            else:
                await channel.send(f"{author} has reported {user}, Reason: {rearray}")
                await ctx.message.delete()
                return


# Server Icon
    @commands.command(aliases = ['sicon', 'Sicon'])
    async def servericon(self, ctx):

        embed=discord.Embed(title="Server Icon", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.set_image(url=f'{ctx.guild.icon_url}')
        await ctx.send(embed=embed)


# Server Banner
    @commands.command(aliases = ['sbanner', 'Sbanner'])
    async def serverbanner(self, ctx):

        banner_url = ctx.guild.banner_url

        embed=discord.Embed(title="Server Banner", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.set_image(url=f'{banner_url}')
        await ctx.send(embed=embed)


# Server Region
    @commands.command(aliases = ['sregion', 'Sregion'])
    async def serverregion(self, ctx):

        region = str(ctx.guild.region)

        embed=discord.Embed(title="Server Location", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="Location:", value=region, inline=False)
        await ctx.send(embed=embed)


# Server ID
    @commands.command(aliases = ['sid', 'Sid'])
    async def serverid(self, ctx):

        id = str(ctx.guild.id)

        embed=discord.Embed(title="Server ID", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="ID:", value=id, inline=False)
        await ctx.send(embed=embed)


# Server Member Count
    @commands.command(aliases = ['MemberCount', 'mcount', 'Mcount'])
    async def membercount(self, ctx):

        member_count = str(ctx.guild.member_count)

        embed=discord.Embed(title="Server Member Count", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="Member:", value=member_count, inline=False)
        await ctx.send(embed=embed)
        

# Error Handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            await ctx.send(f"{ctx.author.mention} Command not found. Please use '--help' to display all current commands.")
            return

        elif isinstance(error, commands.NSFWChannelRequired):
            await ctx.send(f"{ctx.author.mention}, the channel requires NSFW to be enabled for '--{ctx.command}' command.")

        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"The bot is currently missing premissions for '{ctx.command}', please add the premissions first.")

        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"The incorrect argument has been used for '{ctx.command}', please try again or use: ```--help {ctx.command}```")

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(client):
    client.add_cog(info(client))