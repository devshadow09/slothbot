
from ast import Return
from http import client
import token
from tokenize import Token
import nextcord
from nextcord.ext import commands
import aiohttp
import random
from itertools import cycle


TESTING_GUILD_ID = 944494522132496435

token = "MTAwNTAyNTE4OTgwMjgwMzIwMQ.GfrasH.hIJZ5ga-g0jFaTzIa2EtFWuU-7HrAC3Zhgoi_4"


bot = commands.Bot()
client = nextcord.Client()



@bot.event
async def on_ready():
    print(f'bot online as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send(f"Hello! {interaction.user}")






@bot.slash_command(description= "version and changelog of bot", guild_ids=[TESTING_GUILD_ID])
async def version(interaction: nextcord.Interaction):
        embedVar = nextcord.Embed(title="Version and Changelog", description="shadow.py v0.52 Open Beta", color=0x1395ec)
        embedVar.set_author(name = "shadow.py" , icon_url= "https://imgur.com/5GFEQey")
        embedVar.add_field(name="Version", value="0.52 Beta", inline=False)
        embedVar.add_field(name="Changelog", value="to be added", inline=False)
        embedVar.add_field(name="Release name", value="BELPHANT p1", inline=False)
        embedVar.set_footer(text= "Made by Drabshadow#7549. Open sourced on Github!")
        await interaction.send(embed=embedVar)


@bot.slash_command(description= "Get a meme from r/dankmemes subreddit", guild_ids= [TESTING_GUILD_ID])
async def dankmeme(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await interaction.send(embed=embed)

@bot.slash_command(description= "Get a meme from the og r/memes subreddit", guild_ids= [TESTING_GUILD_ID])
async def meme(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await interaction.send(embed=embed)


@bot.slash_command(description= "uno reverse card", guild_ids= [TESTING_GUILD_ID])
async def unoreverse(interaction: nextcord.Interaction):
    embedVar = nextcord.Embed(title = "Uno Reverse", description= "uno reverse")
    embedVar.set_image(url = "https://tenor.com/2Qxl.gif")
    await interaction.send(embed= embedVar)

@bot.slash_command(description= "uno legendary reverse card", guild_ids= [TESTING_GUILD_ID])
async def legend_unoreverse(interaction: nextcord.Interaction):
    embedVar = nextcord.Embed(title = "Uno Legendary Reverse", description= "uno legendary reverse")
    embedVar.set_image(url = "https://tenor.com/bKTI8.gif")
    await interaction.send(embed= embedVar)

cf = 1,0
@bot.slash_command(description= "Heads or Tails?", guild_ids= [TESTING_GUILD_ID])
async def coinflip(interaction: nextcord.Interaction):
    if random.choice(cf) == 1:
        embed= nextcord.Embed(title = "Heads!!!" , description= " You  Got heads!")
        await interaction.send(embed= embed)
    else:
        embedVar= nextcord.Embed(title = "Tails!!" , description= "You  Got tails!")
        await interaction.send(embed= embedVar)

@bot.slash_command(description = "list of all commands", guild_ids= [TESTING_GUILD_ID])
async def help(interaction: nextcord.Interaction):
    embed= nextcord.Embed(title= "List of all commands" )
    embed.add_field(name= "/hello" , value= " says hello with your username" , inline= True)
    embed.add_field(name= "/version" , value= "Shows version and changelog" , inline= True)
    embed.add_field(name= "/meme and /dankmeme" , value= "shows memes from r/meme and r/dankmemes" , inline = False)
    embed.add_field(name= " /unoreverse and /legend_unoreverse" , value= "shows uno reverse gifs" , inline = True)
    embed.add_field(name= "/coinflip" , value= "Flips a coin" , inline = True)
    await interaction.send(embed= embed)

@bot.slash_command(description= "Server info", guild_ids= [TESTING_GUILD_ID])
async def serverinfo(interaction: nextcord.Interaction):
    guild = nextcord.Guild
    embed= nextcord.Embed(title= f"{guild.name}'s info")
    embed.add_field(name= "Owner name" , value= f"{guild.owner_id}" , inline = True )
    embed.add_field(name= "Description" , value= f"{guild.description}" , inline = False)
    embed.add_field(name= "Verification level" , value= f"{guild.verification_level}" , inline = False)
    embed.add_field(name= "Notification settings" , value= f"{guild.default_notifications}" , inline = True)
    embed.add_field(name= "Unlocked Perks" , value= f"{guild.features}" , inline = False)
    embed.add_field(name= "Boost number and tier" , value= f"boosts - {guild.premium_subscription_count} , tier - {guild.premium_tier}" , inline = True)
    embed.add_field(name= "Members" , value= f"{guild.members}" , inline = True)
    embed.add_field(name= "Humans" , value= f"{guild.humans}" , inline = True)
    embed.add_field(name= "Approx Online members" , value= f"{guild.approximate_presence_count}" , inline = True)
    embed.add_field(name= "Text channel count" , value= f"{guild.text_channels}" , inline = True)
    embed.add_field(name= "Voice channel count" , value= f"{guild.voice_channels}" , inline = True)
    embed.add_field(name= "Category count" , value= f"{guild.categories}" , inline = True)
    embed.add_field(name= "Created at " , value= f"{guild.created_at}" , inline = True)
    await interaction.send(embed= embed)

bot.run(token)
