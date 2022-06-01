import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from lib.Ratp import Ratp

ratp = Ratp()

load_dotenv()

token = getenv('SECRET_TOKEN')

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

@bot.event
async def on_ready():
  print('running')

@bot.command()
async def lignes(ctx, type):  
  lines = ratp.get_lines(type)

  used_codes = []

  embed = discord.Embed(title = "Toutes les lignes", color = 0xffffff)

  for line in lines:
    code = line['code']

    if code in used_codes:
      used_codes.append(code)
      continue
    
    used_codes.append(code)
    embed.add_field(name = line['name'], value = line['directions'])

  await ctx.reply(embed = embed)

@bot.command()
async def stations(ctx, type, code):
  stations = ratp.get_stations(type, code)

  stations_list = []

  for station in stations:
    stations_list.append(station['name'])

  embed = discord.Embed(title = f"Toutes les stations de la ligne {code}", description = '\n'.join(stations_list), color = 0xffffff)

  await ctx.reply(embed = embed)

@bot.command()
async def traffic(ctx, type, code):
  traffic = ratp.get_traffic(type, code)

  embed = discord.Embed(title = f"Le traffic sur la ligne {code}", description = traffic, color = 0xffffff)

  await ctx.reply(embed = embed)

@bot.command()
async def prochains(ctx, type, code, station, way = 'aller-retour'):
  schedules = ratp.get_schedules(type, code, station, way)

  embed = discord.Embed(title = f"Les prochains trains à la station {station} de la ligne {code}", color = 0xffffff)

  for schedule in schedules:
    embed.add_field(name = 'Heure', value = schedule['message'])
    embed.add_field(name = 'ㅤ', value = 'ㅤ')
    embed.add_field(name = 'Destination', value = schedule['destination'])

  await ctx.reply(embed = embed)

@bot.command()
async def commandes(ctx):
  commands = {
    "!commandes": "Liste toutes les commandes.",
    "!lignes [metros|rers]": "Liste toutes les lignes de métro ou de RER.",
    "!stations [metros|rers] [<line number>]": "Liste toutes les stations d'une ligne",
    "!traffic [metros|rers] [<line number>]": " Donne les informations à propos du traffic d'une ligne.",
    "!prochains [metros|rers] [<line number>] [<station name>]": "Liste les prochains passages d'un train.",
  }

  embed = discord.Embed(title = f"Commandes", color = 0xffffff)

  for command in commands:
    embed.add_field(name = command, value = commands[command], inline = False)

  await ctx.reply(embed = embed)

bot.run(token)