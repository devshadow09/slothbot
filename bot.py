import nextcord
from nextcord.ext import commands
import aiohttp
import random
from io import BytesIO
import base64
import time



token = "token here"


bot = commands.Bot(intents=nextcord.Intents.all)
client = nextcord.Client()


@bot.event
async def on_ready():
    print(f'bot online as {bot.user}')
    

@bot.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.send(f"Hello! {interaction.user}")




            
@bot.slash_command(description= "version and changelog of bot")
async def version(interaction: nextcord.Interaction):
        embedVar = nextcord.Embed(title="Version and Changelog", description="shadow.py v0.52 Open Beta", color=0x1395ec)
        embedVar.set_author(name = "shadow.py" , icon_url= "https://imgur.com/5GFEQey")
        embedVar.add_field(name="Version", value="0.52 Beta", inline=False)
        embedVar.add_field(name="Changelog", value="to be added", inline=False)
        embedVar.add_field(name="Release name", value="BELPHANT p1", inline=False)
        embedVar.set_footer(text= "Made by Drabshadow#7549. Open sourced on Github!")
        await interaction.send(embed=embedVar)


@bot.slash_command(description= "Get a meme from r/dankmemes subreddit")
async def dankmeme(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await interaction.send(embed=embed)

@bot.slash_command(description= "Get a meme from the og r/memes subreddit")
async def meme(interaction: nextcord.Interaction):
    embed = nextcord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await interaction.send(embed=embed)


@bot.slash_command(description= "uno reverse card")
async def unoreverse(interaction: nextcord.Interaction):
    embedVar = nextcord.Embed(title = "Uno Reverse", description= "uno reverse")
    embedVar.set_image(url = "https://tenor.com/2Qxl.gif")
    await interaction.send(embed= embedVar)

@bot.slash_command(description= "uno legendary reverse card")
async def legend_unoreverse(interaction: nextcord.Interaction):
    embedVar = nextcord.Embed(title = "Uno Legendary Reverse", description= "uno legendary reverse")
    embedVar.set_image(url = "https://tenor.com/bKTI8.gif")
    await interaction.send(embed= embedVar)

cf = 1,0
@bot.slash_command(description= "Heads or Tails?")
async def coinflip(interaction: nextcord.Interaction):
    if random.choice(cf) == 1:
        embed= nextcord.Embed(title = "Heads!!!" , description= " You  Got heads!")
        await interaction.send(embed= embed)
    else:
        embedVar= nextcord.Embed(title = "Tails!!" , description= "You  Got tails!")
        await interaction.send(embed= embedVar)

@bot.slash_command(description = "list of all commands")
async def help(interaction: nextcord.Interaction):
    embed= nextcord.Embed(title= "List of all commands" )
    embed.add_field(name= "/hello" , value= " says hello with your username" , inline= True)
    embed.add_field(name= "/version" , value= "Shows version and changelog" , inline= True)
    embed.add_field(name= "/meme and /dankmeme" , value= "shows memes from r/meme and r/dankmemes" , inline = False)
    embed.add_field(name= " /unoreverse and /legend_unoreverse" , value= "shows uno reverse gifs" , inline = True)
    embed.add_field(name= "/coinflip" , value= "Flips a coin" , inline = True)
    embed.add_field(name= "/serverinfo" , value= "shows server info" , inline = True)
    await interaction.send(embed= embed)

format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@bot.slash_command(description= "server info")

async def serverinfo(ctx : nextcord.Interaction):
    embed = nextcord.Embed(
        color= 0xffffff
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")
    await ctx.send(embed=embed)

class EmbedModal(nextcord.ui.Modal):
	def __init__(self):
		super().__init__(
				"Embed Maker",
			)
			
		self.emTitle = nextcord.ui.TextInput(label = "Embed Title" , min_length = 2, max_length = 50, required = True , placeholder = "enter embed title here")
		self.add_item(self.emTitle)
		
		self.emDesc = nextcord.ui.TextInput(label = "Embed Description" , min_length = 5, max_length = 175, required = True , placeholder = "enter embed title here" , style = nextcord.TextInputStyle.paragraph)
		self.add_item(self.emDesc)
		
		
	async def callback(self, interaction: nextcord.Interaction):
		title = self.emTitle.value
		desc = self.emDesc.value
		em = nextcord.Embed(title = title , description= desc)
		return await interaction.response.send_message(embed = em)
		

@bot.slash_command(description = "an embed",name = "embed")
async def embed(interaction: nextcord.Interaction):
	await interaction.response.send_modal(EmbedModal())

class Dropdown(nextcord.ui.Select):
    def __init__(self , message , images , user):
        self.message = message
        self.images = images
        self.user = user
        options=[
            nextcord.SelectOption(label="1"),
            nextcord.SelectOption(label="2"),
            nextcord.SelectOption(label="3"),
            nextcord.SelectOption(label="4"),
            nextcord.SelectOption(label="5"),
            nextcord.SelectOption(label="6"),
            nextcord.SelectOption(label="7"),
            nextcord.SelectOption(label="8"),
            nextcord.SelectOption(label="9")
        ]
        super().__init__(
            placeholder="choose the image you want to see",
            min_values = 1,
            max_values = 1,
            options = options,
            )
        async def callback(self , interaction: nextcord.Interaction):
            if not int(user) == int(interaction.user.id):
                await interaction.response.send_message("You are not the one who triggered this command!" , emphemeral=True)
            selection = int(self.values[0])-1
            image = BytesIO(base64.decodebytes(self.images[selection].encode("utf-8")))
            return await self.message.edit(content="Content Generated by **craiyon.com**" , file=nextcord.File(image , "image.png") , view = DropdownView(self.message , self.images , self.user))

class DropdownView(nextcord.ui.View):
    def __init__(self , message , images , user):
        super().__init__()
        self.message = message
        self.images = images
        self.user = user
        self.add_item(Dropdown(self.message , self.images , self.user))

@bot.slash_command(description = "ask ai to make an image" , name = "image_gen")
async def image_gen(interaction: nextcord.Interaction , prompt: str):
    ETA = int(time.time() + 60)
    msg = await interaction.send(f"please wait , your image will arive in some time. ETA: <t:{ETA}:R>")
    async with aiohttp.request("POST" , "https://backend.craiyon.com/generate" , json = {"prompt":prompt}) as resp:
        data = await resp.json()
        images = data['images']
        image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
        return await msg.edit(content="Content Generated by **craiyon.com**" , file=nextcord.File(image , "image.png") , view = DropdownView(msg , images , interaction.user.id))



bot.run(token)
