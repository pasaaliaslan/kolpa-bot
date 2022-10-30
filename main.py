import os
import random
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']

INTENTS = discord.Intents.default()
INTENTS.message_content = True


client = commands.Bot(command_prefix="kolpa ", intents=INTENTS)


@client.event
async def on_ready():
    print('sa {0.user}'.format(client))


@client.command()
async def sa(ctx):
    await ctx.send('as')


@client.command(pass_context=True)
async def anlat(ctx, arg=''):
    if arg == '':
        all_audio_files = [f for f in os.listdir('./audio')]
        rand_idx = random.randrange(len(all_audio_files))
        source = FFmpegPCMAudio(f'./audio/{all_audio_files[rand_idx]}')

    else:
        source = FFmpegPCMAudio(f'./audio/{arg}.m4a')

    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        voice.play(source)

    else:
        await ctx.send("Kardeşim bi odaya gir konuşçaz")


@client.command(pass_context=True)
async def sg(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Anliyorum')


try:
    client.run(TOKEN)
except:
    os.system("kill 1")
