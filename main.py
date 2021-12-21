#ApexRandomizer Discord Bot
#Created by Joseph Costello
#Using Python 3.8.6

#Imports
import discord
import random
from discord.ext import commands
from keep_alive import keep_alive

#Sets Bot Command Prefix
client = commands.Bot(command_prefix = '.')

#Initialize
@client.event
async def on_ready():
    print('Bot is ready.')

#Command for Random Location of World's Edge
#Default use: .we
@client.command()
async def we(ctx):
    locations =['Trials', 'Skyhook', 'Survey Camp', 'Climatizer', 'Epicenter', 'Countdown', 'Overlook', 'Fragment West', 'Fragment East', 
                'Landslide', 'Lava Fissure', 'Harvester', 'Staging', 'Thermal Station', 'Tree', 'Lava Siphon', 'Geyser', 'Lava City', 'Launch Site', 'Dome']
    await ctx.send(f'{ctx.author.mention} {random.choice(locations)}')
    
#Command for Random Location of Olympus
#Default use: .oly
@client.command()
async def oly(ctx):
    locations =['Docks', 'Carrier', 'Power Grid', 'Rift', 'Oasis', 'Turbine', 'Energy Depot', 'Gardens', 'Estates', 'Hammond Labs', 
                'Grow Towers', 'Solar Array', 'Orbital Cannon', 'Bonsai Plaza', 'Hydroponics', 'Elysium']
    await ctx.send(f'{ctx.author.mention} {random.choice(locations)}')
    
    
#Command for Random Location of King's Canyon
#Default use: .kc
@client.command()
async def kc(ctx):
    locations =['Crash Site', 'Artillery', 'Spotted Lake', 'Containment', 'Broken Relay', 'The Rig', 'Capacitor', 'Swamps', 
                'The Pit', 'Runoff', 'Bunker', 'Aribase', 'The Cage', 'Labs', 'Hydro Dam', 'Gauntlet', 'Salvage', 'Market', 'Repulsor', 'Water Treatment']
    await ctx.send(f'{ctx.author.mention} {random.choice(locations)}')

#Command for Randomized Weapon Loadout
#Default use: .loadout
@client.command()
async def loadout(ctx):
  weapons = ['HAVOC', 'Flatline', 'Hemlok', 'R-301', 'Alternator', 'Prowler', 'R-99', 'Volt', 'Devotion', 'L-STAR', 'Spitfire', 'Rampage', 'G7 Scout', 'Triple Take', '30-30 Repeater', 'Bocek', 'Charge Rifle', 'Longbow', 'Kraber',' Sentinel', 'EVA-8', 'Mastiff', 'Mozambique', 'Peacekeeper', 'RE-45', 'P2020', 'Wingman']

  supply = ['Alternator', 'Kraber', 'Triple Take', 'Spitfire']

  weap1 = random.choice(weapons)
  weap2 = random.choice(weapons)

  if weap1 == weap2:
    print(f'Rolled same guns: {weap1}')
    weap2 = random.choice(weapons)

  while weap1 in supply:
    print(f'Supply Drop Weapon: {weap1}')
    weap1 = random.choice(weapons)
    print(f'New Gun: {weap1}')
  
  while weap2 in supply:
    print(f'Supply Drop Weapon: {weap2}')
    weap2 = random.choice(weapons)
    print(f'New Gun: {weap2}')

  await ctx.send(f'{ctx.author.mention} {weap1} and {weap2}')

#Command for user lookup on Apex Legends Tracker
##Default use: .stats {platform} {username}
@client.command()
async def stats(ctx,platform, name):
  url = f'https://apex.tracker.gg/apex/profile/{platform}/{name}'
  embed=discord.Embed(title=f'{name} Apex Stats', url = url, description = f'{name} on {platform} Apex Legends Tracker',color=discord.Color.blue() )
  await ctx.send(embed=embed)
  await ctx.send(f'{ctx.author.mention}')
  
#Run code to keep bot alive
keep_alive()

client.run('ODk1NTI5OTY1MDgzMjk1Nzg3.YV55RQ.M9m96rOZQVgy6KkvzZ0h0K3LoaU')
