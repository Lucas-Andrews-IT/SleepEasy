# https://github.com/SleepySlothx/SleepEasyBOT

# Imports
import asyncio
import random
import discord
from discord.ext import commands
from discord.ext.commands.core import command, group, has_permissions

# Importing the preset configuration from config.py
from configuration import config


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client


# Die Command
    @commands.command(aliases=['Die', 'suicide', 'Suicide'])
    async def die(self, ctx):
        async with ctx.channel.typing():
            response = ["a Overdose","a Stroke","AIDS","Malaria","Suicide","starving in a supermarket","driving off a cliff and surviving only to die of shock from the hospital bill",
                        "drowning in Jell-o","trying to eat a whole Big Mac in one bite and choked to death","attempting to fly, whilst high","tried to make toast while having a bath",
                        "getting their face in an egg-beater","heatstroke in the arctic","drinking too much antifreeze","getting stuck in a tanning booth","walking across quicksand while carrying an anvil",
                        "getting stabbed with a cucumber","setting fire to their hair","snapping their neck on an office chair","swallowing too much helium","snoo snoo","playing Russian roulette with a fully loaded Uzi",
                        "playing catch with a knife", "Autoerotic Asphyxiation", "laughing at dad jokes", "suffocation from laughing too much", "getting hit by a meteroite", "stepping on a lego"]
    
            embed=discord.Embed(title=f"{ctx.author.name} has died!", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            embed.add_field(name="Coroner Report:", value=f"Died from {random.choice(response)}.", inline=False)
            embed.set_footer(text=config.EMBED_FOOTER)
    
            await ctx.send(embed=embed)
            return


# Hug Command
    @commands.command(aliases=['hugs', 'Hug', 'Hugs'])
    async def hug(self, ctx, user):
        async with ctx.channel.typing():
            response = ["has kicked them in the balls", "hugged them back", f"has nuzzled {ctx.author.mention} back instead", f"has body slammed {ctx.author.mention} for harrassment",
            f"has taken off all their clothes and hugged {ctx.author.mention} back 😲"]
    
            embed=discord.Embed(color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            embed.add_field(name=f"Two cuties have hugged.", value=f"{ctx.author.mention} has hugged {user}.", inline=False)
            embed.add_field(name=f"Their response", value=f"{user} {random.choice(response)}.", inline=False)
            embed.set_thumbnail(url='https://c.tenor.com/vHw75zknjZMAAAAi/radiofm4-fm4.gif')
            embed.set_footer(text="Awwww. 💕")
    
            await ctx.send(embed=embed)
            return


# Kiss Command
    @commands.command(aliases=['kisses', 'Kiss', 'Kisses'])
    async def kiss(self, ctx, user):
        async with ctx.channel.typing():
            response = ["has unzipped their pants", "kissed them back", f"has nuzzled {ctx.author.mention} back instead and begun making out", "proceeded to go for a kiss back with tongue", "has called the police for sexual assault",
            "just wanted to stay as friends"]

            embed=discord.Embed(color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            embed.add_field(name=f"Two cuties have kissed!", value=f"{ctx.author.mention} has kissed {user}.", inline=False)
            embed.add_field(name=f"Their response", value=f"{user} {random.choice(response)}.", inline=False)
            embed.set_thumbnail(url='https://media4.giphy.com/media/lTQF0ODLLjhza/giphy.gif?cid=ecf05e473cx5srvsn3xmqylgfvvr1dp3ujrh3ihh4914on9k&rid=giphy.gif')
            embed.set_footer(text="Get a room! 💕")
    
            await ctx.send(embed=embed)
            return


# Magic 8ball Command
    @commands.command(aliases=['8ball', 'Magic8ball'])
    async def magic8ball(self, ctx, *, question):
        async with ctx.channel.typing():
            response = ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.",
                        "Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.",
                        "Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.",
                        "My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

            embed=discord.Embed(title="Magic 8Ball", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            embed.add_field(name="Question: ", value=f"{question}", inline=False)
            embed.add_field(name="Answer: ", value=f"{random.choice(response)}", inline=False)
            embed.set_footer(text=config.EMBED_FOOTER)
    
            await ctx.send(embed=embed)
            return


# Gay Calculator Command
    @commands.command(aliases=['gayness','gaycal', 'Gayness','GayCal', 'Gaycal'])
    async def gay(self, ctx, *, question, amount=1):
        async with ctx.channel.typing():
            response = ["1","2","3","4","5","6","7","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
                        "26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44", "45","46","47","48","49","50",
                        "51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75",
                        "76","77","78","79","80","81","82","83", "84","85","86","87","88","89","90","91","92","93","95","96","98","99","100"]
    
            cal_embed=discord.Embed(title="Calculating...", color=config.EMBED_COLOR, font_size=200)
            cal_embed.set_footer(text="")
    
            await ctx.send(embed=cal_embed)
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
    
            done_embed=discord.Embed(title="Gayness Percentage Calculated!", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            done_embed.add_field(name="For", value=f"{question}", inline=False)
            done_embed.add_field(name="Percentage ", value=f"{random.choice(response)}%", inline=False)
            done_embed.set_footer(text=config.EMBED_FOOTER)
    
            await ctx.send(embed=done_embed)
            return


# Homie Calculator Command
    @commands.command(aliases=['homieness','homiecal', 'Homie', 'HomieCal', 'Homieness', 'Homiecal'])
    async def homie(self, ctx, *, question, amount=1):
        async with ctx.channel.typing():
            response = ["1","2","3","4","5","6","7","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
                        "26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44", "45","46","47","48","49","50",
                        "51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75",
                        "76","77","78","79","80","81","82","83", "84","85","86","87","88","89","90","91","92","93","95","96","98","99","100"]
    
            cal_embed=discord.Embed(title="Calculating...", color=config.EMBED_COLOR, font_size=200)
            cal_embed.set_footer(text="")
    
            await ctx.send(embed=cal_embed)
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
    
            done_embed=discord.Embed(title="Homie Percentage Calculated!", color=config.EMBED_COLOR, font_size=200, timestamp=ctx.message.created_at)
            done_embed.add_field(name="For", value=f"{question}", inline=False)
            done_embed.add_field(name="Percentage ", value=f"{random.choice(response)}%", inline=False)
            done_embed.set_footer(text=config.EMBED_FOOTER)
    
            await ctx.send(embed=done_embed)
            return


def setup(client):
    client.add_cog(fun(client))
