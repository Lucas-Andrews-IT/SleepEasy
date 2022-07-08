# https://github.com/SleepySlothx/SleepEasyBOT

# Imports
import sys
import traceback
import aiohttp
import discord
from discord.activity import Spotify
from discord.ext import commands
from discord.ext.commands.core import command

# Importing the preset configuration from config.py
from configuration import config

class images_reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

# Reddit Cute
 # Bird Command
    @commands.command()
    async def bird(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/birdpics') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Lizard Command
    @commands.command()
    async def lizard(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/Lizards') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Kitten Command
    @commands.command()
    async def kitten(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/Kitten') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Snake Command
    @commands.command()
    async def snake(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/snakes') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Puppy Command
    @commands.command()
    async def puppy(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/rarepuppers') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


# Memes
 # funny Command
    @commands.command()
    async def funny(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/funny') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # memes Command
    @commands.command()
    async def memes(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/memes') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Economy Command
    @commands.command()
    async def economy(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/MemeEconomy') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # facebookmemes Command
    @commands.command()
    async def facebook(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/terriblefacebookmemes') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # dankmemes Command
    @commands.command()
    async def dankmemes(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/dankmemes') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # AdviceAnimals Command
    @commands.command()
    async def adviceanimals(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/AdviceAnimals') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # ComedyCemetery Command
    @commands.command()
    async def comedycemetery(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/ComedyCemetery') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


# Reddit NSFW 
 # Rule34 Command
    @commands.command(aliases=['r34'])
    @commands.is_nsfw()
    async def rule34(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/rule34') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return
            

 # Hentai Command
    @commands.command(aliases=['pervert'])
    @commands.is_nsfw()
    async def hentai(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/hentai') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted 
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return
 

 # Hentai Ass Command
    @commands.command(aliases=['hentaiass', 'HentaiAss', 'hentai ass'])
    @commands.is_nsfw()
    async def hass(self, ctx, ):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/AnimeBooty') # Subreddit after 'gimme'
                imagejson = await request.json()

                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted 
                embed.set_footer(text=f"Requested by {ctx.message.author}")

                await ctx.send(embed=embed) # Send the embed
                return


 # Hentai Feet Command
    @commands.command(aliases=['hentaifeet', 'HentaiFeet', 'hentai feet'])
    @commands.is_nsfw()
    async def hfeet(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/hentaifeet') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted 
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Hentai Thicc Command
    @commands.command(aliases=['hentaithicc', 'HentaiThicc', 'hentai thicc'])
    @commands.is_nsfw()
    async def hthicc(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/thick_hentai') # Subreddit after 'gimme'
                imagejson = await request.json()
            
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted 
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Hentai Boobs Command
    @commands.command(aliases=['hentaiboobs', 'HentaiBoobs', 'hentai boobs'])
    @commands.is_nsfw()
    async def hboobs(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/HentaiBoobs') # Subreddit after 'gimme'
                imagejson = await request.json()
                
                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted 
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                
                await ctx.send(embed=embed) # Send the embed
                return


 # Hentai Thighs Command
    @commands.command(aliases=['hentaithighs', 'HentaiThighs', 'hentai thighs'])
    @commands.is_nsfw()
    async def hthighs(self, ctx, ):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                
                request = await session.get('https://meme-api.herokuapp.com/gimme/thighhighhentai') # Subreddit after 'gimme'
                imagejson = await request.json()

                embed = discord.Embed(color=config.EMBED_COLOR, font_size=200) # Create embed
                embed.add_field(name="Title", value=imagejson['title'], inline=False) # Title of the reddit post
                embed.add_field(name="Subreddit", value=imagejson['subreddit'], inline=False) # Subreddit the post is from.
                embed.set_image(url=imagejson['url']) # Set the embed image to the value of the 'value' wanted 
                embed.set_footer(text=f"Requested by {ctx.message.author}")

                await ctx.send(embed=embed) # Send the embed
                return

def setup(client):
    client.add_cog(images_reddit(client))
