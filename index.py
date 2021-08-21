# CodeBlocks
import discord
import random
from discord.ext import commands
from random import choice 

TOKEN = "PASTE THE TOKEN"
client = commands.Bot(command_prefix = "$")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("CodeBlocks | $help"))
    print(f"[Discord API] Connected To [{client.user}]")

@client.command()
async def help(ctx):
    await ctx.channel.send("""> **$ping | Shows Ping.**
            > **$info | Shows Info.**
            > **$ban | Bans Members.**
            > **$unban | Unbans Members.**
            > **$kick | Kicks Members.**
            > **$8ball | Plays 8ball.**
            > **$coinflip | Plays CoinFlip.**""", delete_after=10)
    await ctx.message.delete()

@client.command()
async def info(ctx):
    await ctx.channel.send("""> **Creator: Azlo**
            > **Created: 21-08-2021**
            > **Last Updated: 21-08-2021**
            > **Language: Python3**""", delete_after=10)
    await ctx.message.delete()

@client.command()
async def ping(ctx):
    await ctx.channel.send(f"**MS:** {round(client.latency * 1000)}", delete_after=5)
    await ctx.message.delete()

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.channel.send("**User was banned.**", delete_after=5)
    await ctx.message.delete()

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.channel.send("**User was kicked.**", delete_after=5)
    await ctx.message.delete()

client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"**Unbanned** {user.mention}", delete_after=5)
            await ctx.message.delete()
            return

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

determine_flip = [1, 0]

@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip | CodeBlocks", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip | CodeBlocks", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
        await ctx.send(embed=embed)



client.run(TOKEN)
