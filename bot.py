from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

TOKEN = "Add your TOKEN here"
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('Ready to use')

@bot.command(pass_context=True)
async def test(ctx, id):
    user_id = int(id)
    author_id = ctx.message.author.id
    author_name = '<@' + str(author_id) + '>'
    member = ctx.message.guild.get_member(user_id)
    
    if member:
        display_name = member.display_name
        await ctx.channel.send('{} -> username : **{}**'.format(author_name, member))
        print("username is {}".format(member))
    else:
        print("not found this user")

bot.run(TOKEN)