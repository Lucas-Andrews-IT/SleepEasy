# https://github.com/SleepySlothx/SleepEasyBOT

# Imports
import asyncio
import discord
from discord import Guild, client, member
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command

# Importing the preset configuration from config.py
from configuration import config


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


# Clear Chat Command    
    @commands.command(aliases = ['cc', 'clearchat'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=16):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"{amount} messages have been purged!", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        await ctx.reply(embed=embed)


# Mute Command
    @commands.command(aliases = ['m', 'Mute'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="In Jail")

        if not mutedRole:
            mutedRole = await guild.create_role(name="In Jail")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        
        embed = discord.Embed(title="Muted", description=f"{member.mention} was sent to jail ", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.set_footer(text="Task Completed!")
        
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" You have been muted from {guild.name} Reason: {reason}")


# Temp Mute Command
    @commands.command(aliases = ['tm', 'tmute', 'TempMute', 'Tmute'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def tempmute(self, ctx, member: discord.Member, time, d, reason=None): 
        
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
	            
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
	    
        await member.add_roles(mutedRole)
        
        embed = discord.Embed(title="Muted!", description=f"{member.mention} has been sent to jail.", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.add_field(name="Time left for the mute:", value=f"{time}{d}", inline=False)
	    
        await ctx.reply(embed=embed)
        if d == "s":
            await asyncio.sleep(int(time))
        if d == "m":								
            await asyncio.sleep(int(time*60))
        if d == "h":
            await asyncio.sleep(int(time*60*60))
        if d == "d":
            await asyncio.sleep(int(time*60*60*24))
	    
        await member.remove_roles(mutedRole)
        embed = discord.Embed(title="Unmuted!", description=f"Unmuted {member.mention}. ", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        await ctx.reply(embed=embed)


# Unmute Command
    @commands.command(aliases = ['umute', 'UnMute', 'Umute'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def unmute(self, ctx, member: discord.Member):
        
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        
        await member.remove_roles(mutedRole)
        await member.send(f" You have released from jail in {ctx.guild.name}")
        
        embed = discord.Embed(title="Unmute", description=f" Unmuted: \n{member.mention}", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.set_footer(text="Task Completed!")
        
        await ctx.send(embed=embed)


# Kick Command
    @commands.command(aliases=["remove"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        
        await member.kick(reason=reason)
        
        embed = discord.Embed(title="Kicked Member", description=f" {member.mention} was kicked.\n", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="Reason: ", value=reason, inline=False)
        embed.set_footer(text="Task Completed!")
        
        await ctx.send(embed=embed)
        return


# Ban Command
    @commands.command(aliases=["hammer"])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        
        await member.ban(reason=reason)

        embed = discord.Embed(title="Banned Member", description=f" {member.mention} was ban.\n", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="Reason: ", value=reason, inline=False)
        embed.set_footer(text="Task Completed!")

        await ctx.send(embed=embed)
        return


# Unban Command
    @commands.command(aliases = ['uban', 'Uban', 'Unban'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_user:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                embed = discord.Embed(title="Unbanned Member", description=f" {member.mention} was unban.\n", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
                embed.set_footer(text="Task Completed!")

                await ctx.send(embed=embed)
            return


# Temp Ban Command
    @commands.command(aliases = ['tban', 'Tempban', 'TempBan', 'Tban'])
    @commands.has_permissions(kick_members=True)
    async def tempban(self, ctx, member: discord.Member, time, d, *, reason="No Reason"):
        if member == None:
            embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
            await ctx.reply(embed=embed)
			
        else:
            guild = ctx.guild
            embed = discord.Embed(title="Banned!", description=f"{member.mention} has been banned!", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            embed.add_field(name="Reason: ", value=reason, inline=False)
            embed.add_field(name="Time left for the ban:", value=f"{time}{d}", inline=False)
            await ctx.reply(embed=embed)
            await guild.ban(user=member)

            # before each time variable ensure int before and close.
            if d == "s":
                await asyncio.sleep(int(time))
                await guild.unban(user=member)
            if d == "m":
                await asyncio.sleep(int(time*60))
                await guild.unban(user=member)
            if d == "h":
                await asyncio.sleep(int(time*60*60))
                await guild.unban(user=member)
            if d == "d":
                await asyncio.sleep(time*60*60*24)
                await guild.unban(int(user=member))


# Nuke Channel Command
# Credits to fork#3178 on the 10/08/2021 @ 3:49AM
    @commands.command(aliases = ['nukec', 'Nukec', 'NukeC', 'nuke'])
    @commands.has_permissions(manage_channels=True)
    async def nukechannel(self, ctx, channel: discord.TextChannel = None):
        
        guild = Guild.channels
        
        if channel == None: 
            await ctx.send("you did not mention a channel.")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="has been nuked")
            await nuke_channel.delete()
            embed=discord.Embed(title='This channel has been nuked.', color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            embed.set_image(url='https://media.tenor.com/images/4ea982fcfce49e57a7e04820f9b80b0a/tenor.gif') # Fixed Link
            await new_channel.send(embed=embed)
            await ctx.send(f"nuked {channel.name} without any issues")

        else:
            await ctx.send(f"no channel named {channel.name} was found")
            

def setup(client):
    client.add_cog(moderation(client))
