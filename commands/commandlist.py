# https://github.com/SleepySlothx/SleepEasyBOT

# Imports
import discord
from discord.ext import commands

# Importing the preset configuration from config.py
from configuration import config


class commandlist(commands.Cog):
    def __init__(self, client):
        self.client = client


# Display Command List
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
    
    # Head
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
    
    # Category 1
        embed.add_field(name="General", value="info\npoll\ninvite\nreigon\nserverid\nservericon\nserverbanner\nmembercount", inline=True)
        embed.add_field(name="Fun", value="die\nhug\nkiss\n8ball\ngaycal\nhomiecal", inline=True)
        embed.add_field(name="Moderation", value="ban\nkick\nclear\nmute\nunban\nunmute\ntempban\ntempmute\nnukechannel", inline=True)
        
    # Category 2
        embed.add_field(name="Cute", value="bird\nlizard\nkitten\nsnake\npuppy", inline=True)
        embed.add_field(name="Meme", value="funny\nmemes\neconomy\nfacebook\ndankmemes\nadviceanimals\ncomedycemetery", inline=True)
        embed.add_field(name="NSFW", value="rule34\nhentai\nhass\nhfeet\nhthicc\nhboobs\nhthighs", inline=True)
        
    # Description
    
        embed.add_field(name="Get Description", value="Use {}help [command] for extended information.".format(config.BOT_PREFIX) + f" {ctx.author.mention}", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

# info.py
# General Descriptions
 # Info Help
    @help.command(aliases=['botinfo'])
    async def info(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}info".format(config.BOT_PREFIX), value=f"Display all current information about this bot.", inline=False)
        embed.add_field(name="Aliases: ", value=f"botinfo", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Poll Help
    @help.command(aliases=['vote'])
    async def poll(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}poll".format(config.BOT_PREFIX), value=f'Creates a question within a string of "question" and 2 options.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--poll "Sleepy Manager is awesome" yes no', inline=False)
        embed.add_field(name="Aliases: ", value=f"vote", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Invite Help
    @help.command(aliases=['addbot', 'invitebot'])
    async def invite(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}invite".format(config.BOT_PREFIX), value=f"This will generate a message that allows you to invite to your own discord servers.", inline=False)
        embed.add_field(name="Aliases: ", value=f"addbot\ninvitebot", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Report Help
    @help.command(aliases=['rep'])
    async def report(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}report".format(config.BOT_PREFIX), value=f'This command will report users to the dedicated staff chat.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--report @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"rep", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Server Icon Help
    @help.command(aliases=['sicon', 'Sicon'])
    async def servericon(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}servericon".format(config.BOT_PREFIX), value=f'Displays the server icon, if it has one.', inline=False)
        embed.add_field(name="Aliases: ", value=f"sicon\nSicon", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Server Banner Help
    @help.command(aliases=['sbanner', 'Sbanner'])
    async def serverbanner(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}serverbanner".format(config.BOT_PREFIX), value=f'Displays the server banner, if it has one by having nitro applied.', inline=False)
        embed.add_field(name="Aliases: ", value=f"sbanner\nSbanner", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Server Region Help
    @help.command(aliases=['sregion', 'Sregion'])
    async def serverregion(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}serverregion".format(config.BOT_PREFIX), value=f'Displays the server region.', inline=False)
        embed.add_field(name="Aliases: ", value=f"sregion\nSregion", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Server ID Help
    @help.command(aliases=['sid', 'Sid'])
    async def serverid(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}serverid".format(config.BOT_PREFIX), value=f'Displays the server ID.', inline=False)
        embed.add_field(name="Aliases: ", value=f"sid\nSid", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Member Count Help
    @help.command(aliases=['MemberCount', 'mcount', 'Mcount'])
    async def membercount(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}membercount".format(config.BOT_PREFIX), value=f'Displays the server member count.', inline=False)
        embed.add_field(name="Aliases: ", value=f"MemberCount\nmcount\nMcount", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

# fun.py
# Fun Descriptions
 # Die Help
    @help.command(aliases=['Die', 'suicide', 'Suicide'])
    async def die(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}die".format(config.BOT_PREFIX), value=f"Various stupid ways to die.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--die', inline=False)
        embed.add_field(name="Aliases: ", value=f"Die\nsuicide\nSuicide", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Hug Help
    @help.command(aliases=['hugs', 'Hug', 'Hugs'])
    async def hug(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}hug".format(config.BOT_PREFIX), value=f"Hugs the mentioned user with their response back.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--hug @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"Hug\nhugs\nHugs", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Kiss Help
    @help.command(aliases=['kisses', 'Kiss', 'Kisses'])
    async def kiss(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}kiss".format(config.BOT_PREFIX), value=f"Kiss the mentioned user.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--kiss @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"Kiss\nkisses\nKisses", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # 8Ball Help
    @help.command(aliases=['magic8ball', 'Magic8ball'])
    async def _8ball(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}8ball".format(config.BOT_PREFIX), value=f"Fortune-telling or seeking advice.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--8ball (question)', inline=False)
        embed.add_field(name="Aliases: ", value=f"magic8ball\nMagic8ball\n8Ball", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Gay Calculator Help
    @help.command(aliases=['gayness', 'Gayness','GayCal', 'Gaycal'])
    async def gaycal(self, ctx):

        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}gaycal".format(config.BOT_PREFIX), value=f"Calculates the precentage of how gay mentioned user is for you.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--gaycal @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"gayness\ngaycal\nGayness\nGayCal\nGaycal", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Homie Calculator Help
    @help.command(aliases=['homieness', 'Homie', 'HomieCal', 'Homieness', 'Homiecal'])
    async def homiecal(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}homiecal".format(config.BOT_PREFIX), value=f"Calculates the precentage of how much a homie the mentioned user is potentially.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--homiecal @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"homieness\nhomiecal\nHomie\nHomieCal\nHomiecal", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

# moderation.py
# Moderation Descriptions
 # Clear Help
    @help.command(aliases = ['cc', 'clearchat'])
    async def clear(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}clear".format(config.BOT_PREFIX), value=f"The clear command will remove up to 8 messages or the amount set after the command.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--clear (amount)', inline=False)
        embed.add_field(name="Aliases: ", value=f"cc\nclearchat", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Mute Help
    @help.command(aliases = ['m', 'Mute'])
    async def mute(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}mute".format(config.BOT_PREFIX), value=f"This command is for moderators to mute mentioned user.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--mute @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"m\nMute", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)
    
        await ctx.send(embed=embed)
        return

 # Temp Mute Help
    @help.command(aliases = ['tm', 'tmute', 'TempMute', 'Tmute'])
    async def tempmute(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}tempmute".format(config.BOT_PREFIX), value='Similar to "mute", but with a timer.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--tempmute @user amount s,m,h,d "reason"', inline=False)
        embed.add_field(name="Aliases: ", value=f"tm\ntmute\nTmute\nTempMute", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Unmute Help
    @help.command(aliases = ['umute', 'UnMute', 'Umute'])
    async def unmute(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}unmute".format(config.BOT_PREFIX), value=f"This command is for moderators to unmute mentioned user.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--unmute @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"umute\nUnMute\nUmute", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Kick Help
    @help.command(aliases=["remove"])
    async def kick(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}kick".format(config.BOT_PREFIX), value=f"This command is for moderators to kick mentioned user from the server.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--kick @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"remove", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Ban Help
    @help.command(aliases=["hammer"])
    async def ban(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}ban".format(config.BOT_PREFIX), value=f"This command is for moderators to ban mentioned user from the server.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--ban @user', inline=False)
        embed.add_field(name="Aliases: ", value=f"hammer", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Unban Help
    @help.command(aliases = ['uban', 'Uban', 'Unban'])
    async def unban(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}unban".format(config.BOT_PREFIX), value=f"This command is for moderators to unban UserID from the server.", inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--unban userID', inline=False)
        embed.add_field(name="Aliases: ", value=f"uban\nUban\nUnban", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Temp Ban Help
    @help.command(aliases = ['tban', 'Tempban', 'TempBan', 'Tban'])
    async def tempban(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}tempban".format(config.BOT_PREFIX), value=f'Similar to "ban", but with a timer.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--tempban @user amount s,m,h,d "reason"', inline=False)
        embed.add_field(name="Aliases: ", value=f"tban\nTban\nTempban\nTempBan", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Nuke Channel Help
    @help.command(aliases = ['nukec'])
    async def nukechannel(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}nukechannel".format(config.BOT_PREFIX), value=f'This command is used by the owner to clone an entire channel and its premissions and delete the old one.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--nukechannel #channelname', inline=False)
        embed.add_field(name="Aliases: ", value=f"nukec\nNukec\nNukeC", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

# Reddit.py
# Cute
 # Bird Help
    @help.command()
    async def bird(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}bird".format(config.BOT_PREFIX), value=f'This command is used to display birds from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--bird', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Lizard Help
    @help.command()
    async def lizard(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}lizard".format(config.BOT_PREFIX), value=f'This command is used to display lizards from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--lizard', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Kitten Help
    @help.command()
    async def kitten(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}kitten".format(config.BOT_PREFIX), value=f'This command is used to display kittens from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--kitten', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Snake Help
    @help.command()
    async def snake(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}snake".format(config.BOT_PREFIX), value=f'This command is used to display snakes from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--snake', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Puppy Help
    @help.command()
    async def puppy(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}puppy".format(config.BOT_PREFIX), value=f'This command is used to display puppys from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--puppy', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

# Memes
 # 5050 Help
    @help.command(aliases = ['fiftyfifty', 'FiftyFifty'])
    async def _5050(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}5050".format(config.BOT_PREFIX), value=f'This command is used to display memes from fiftyfifty subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--5050', inline=False)
        embed.add_field(name="Aliases: ", value=f"fiftyfifty\nFiftyFifty", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

 # Funny Help
    @help.command()
    async def funny(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}funny".format(config.BOT_PREFIX), value=f'This command is used to display memes from funny subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--funny', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Memes Help
    @help.command()
    async def memes(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}memes".format(config.BOT_PREFIX), value=f'This command is used to display memes from memes subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--memes', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Economy Help
    @help.command()
    async def economy(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}economy".format(config.BOT_PREFIX), value=f'This command is used to display memes from economymemes subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--economy', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Facebook Help
    @help.command()
    async def facebook(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}facebookmemes".format(config.BOT_PREFIX), value=f'This command is used to display memes from terriblefacebookmemes subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--facebookmemes', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Dankmemes Help
    @help.command()
    async def dankmemes(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}dankmemes".format(config.BOT_PREFIX), value=f'This command is used to display memes from dankmemes subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--dankmemes', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Advice Animals Help
    @help.command()
    async def adviceanimals(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}adviceanimals".format(config.BOT_PREFIX), value=f'This command is used to display memes from AdviceAnimals subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--adviceanimals', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Comedy Cemetry Help
    @help.command()
    async def comedycemetery(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}comedycemetery".format(config.BOT_PREFIX), value=f'This command is used to display memes from comedycemetery subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--comedycemetery', inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return

# NSFW
 # Rule34 Help
    @help.command(aliases = ['r34'])
    async def rule34(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}rule34".format(config.BOT_PREFIX), value=f'This command is used to display Rule34 images from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--rule34', inline=False)
        embed.add_field(name="Aliases: ", value=f"r34", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Hentai Help
    @help.command(aliases = ['pervert'])
    async def hentai(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}hentai".format(config.BOT_PREFIX), value=f'This command is used to display Hentai images from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--hentai', inline=False)
        embed.add_field(name="Aliases: ", value=f"pervert", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Hentai Boobs Help
    @help.command(aliases=['hentaiboobs', 'HentaiBoobs', 'hentai boobs'])
    async def hboobs(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}hentaiboobs".format(config.BOT_PREFIX), value=f'This command is used to display Hentai Boobs images from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--hentaiboobs', inline=False)
        embed.add_field(name="Aliases: ", value=f"hentaiboobs\nHentaiBoobs\nhentai boobs", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Hentai Thicc Help
    @help.command(aliases=['hentaithicc', 'HentaiThicc', 'hentai thicc'])
    async def hthicc(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}hentaithicc".format(config.BOT_PREFIX), value=f'This command is used to display Hentai Thicc images from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--hentaithicc', inline=False)
        embed.add_field(name="Aliases: ", value=f"hentaithicc\nHentaiThicc\nhentai thicc", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Hentai Feet Help
    @help.command(aliases=['hentaifeet', 'HentaiFeet', 'hentai feet'])
    async def hfeet(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}hentaigif".format(config.BOT_PREFIX), value=f'This command is used to display Hentai Feet from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--hentaifeet', inline=False)
        embed.add_field(name="Aliases: ", value=f"hentaifeet\nHentaiFeet\nhentai feet", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


 # Hentai Thighs Help
    @help.command(aliases=['hentaithighs', 'HentaiThighs', 'hentai thighs'])
    async def hthighs(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}hentaithighs".format(config.BOT_PREFIX), value=f'This command is used to display Hentai Thighs from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--hentaifeet', inline=False)
        embed.add_field(name="Aliases: ", value=f"hentaifeet\nHentaiFeet\nhentai feet", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


    @help.command(aliases=['hentaiass', 'HentaiAss', 'hentai ass'])
    async def hass(self, ctx):
        embed=discord.Embed(title="Help Command", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
        embed.add_field(name="{}hentaiass".format(config.BOT_PREFIX), value=f'This command is used to display Hentai Thighs from a subreddit.', inline=False)
        embed.add_field(name="Example: ".format(config.BOT_PREFIX), value=f'--hentaiass', inline=False)
        embed.add_field(name="Aliases: ", value=f"hentaiass\nHentaiAss\nhentai ass", inline=False)
        embed.set_footer(text=config.EMBED_FOOTER)

        await ctx.send(embed=embed)
        return


def setup(client):
    client.add_cog(commandlist(client))
