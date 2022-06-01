import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from lib.Ratp import Ratp

ratp = Ratp()

load_dotenv()

token = getenv('SECRET_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
  print('running')

@bot.command()
async def lines(ctx, type):  
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
async def schedules(ctx, type, code, station):
  schedules = ratp.get_schedules(type, code, station)

  embed = discord.Embed(title = f"Les prochains trains à la station {station} de la ligne {code}", color = 0xffffff)

  for schedule in schedules:
    embed.add_field(name = 'Heure', value = schedule['message'])
    embed.add_field(name = 'Destination', value = schedule['destination'])

  await ctx.reply(embed = embed)

@bot.command()
  async def help(ctx, type)
  command =
  {
  "!lines":"affiches toutes les lignes",
  "!lines metros":"affiches toutes les lignes de métro",
  "!lines rers":"affiches toutes les lignes de rer",
  "!stations":"!stations suivis du numéro de la ligne donne le noms des stations sur cette ligne "
  "!traffic ligne + stations":"Donne les informations sur le traffic en temps réel"
  "!schedule ligne + stations":"heure d'arrivé des prochains trains"

bot.run(token)
