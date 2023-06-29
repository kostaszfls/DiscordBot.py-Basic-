import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'Welcome, {member.mention}!')

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(f'Pong! Latency: {round(latency * 1000)}ms')

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.name} has been kicked.')

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.name} has been banned.')

@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    # Implement your own logic for issuing warnings
    await ctx.send(f'{member.name} has been warned for {reason}.')

@bot.command()
async def timeout(ctx, member: discord.Member, duration: int, *, reason=None):
    # Implement your own logic for timing out members
    await ctx.send(f'{member.name} has been timed out for {duration} seconds due to {reason}.')

@bot.command()
async def clear(ctx, amount=5):
    # Implement your own logic for clearing messages
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'{amount} messages cleared.', delete_after=5)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands", color=discord.Color.blue())
    embed.add_field(name="!ping", value="Check the bot's latency", inline=False)
    embed.add_field(name="!kick <user>", value="Kick a user from the server", inline=False)
    embed.add_field(name="!ban <user>", value="Ban a user from the server", inline=False)
    embed.add_field(name="!warn <user> <reason>", value="Issue a warning to a user", inline=False)
    embed.add_field(name="!timeout <user> <duration> <reason>", value="Timeout a user for a specified duration", inline=False)
    embed.add_field(name="!clear [amount]", value="Clear a specified number of messages (default: 5)", inline=False)

    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
