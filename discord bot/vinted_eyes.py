import os
import discord
from discord import Embed, app_commands
from discord.ext import commands
from dotenv import load_dotenv
import re
from datetime import datetime, timezone

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


class MyGroup(app_commands.Group):
    ...


mygroup = MyGroup(name="greetings", description="Welcomes users and interact with them.")

targeted_links = []


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} ({bot.application_id})')
    print(f"Guild ID: {bot.guilds[0].id}")

    bot.tree.add_command(mygroup)

    bot.tree.copy_global_to(guild=GUILD_ID)
    await bot.tree.sync(guild=GUILD_ID)

    print('-------------------------------------------------------')


@bot.event
async def on_message(message):
    print(f"message from {message.author}: {message.content}")

    if message.author == bot.user:
        return

    if str.lower(message.content).startswith("bonjour"):
        await message.channel.send('Salut bg')

    # Nécessaire pour que les commandes fonctionnent en plus de on_message
    await bot.process_commands(message)


@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return

    await before.channel.send(f"message édité: {before.content} -> {after.content}")


@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return

    await message.channel.send(f"message supprimé: {message.content}")


@bot.hybrid_command()
async def test(ctx, arg):
    await ctx.send(arg)


@mygroup.command(name="ping", description="Just reply with pong in DM")
async def ping(interaction: discord.Interaction):
    await interaction.message.author.send("pong")


@mygroup.command(name="ciao", description="Say goodbye to leavers")
async def ciao(interaction: discord.Interaction):
    await interaction.response.send_message(f"Ciao! {interaction.user.mention}", ephemeral=True)


@mygroup.command()
async def target(interaction:discord.Interaction, arg: str):
    if arg not in targeted_links:
        if re.search(r"https://www\.vinted\.(fr|com)/api/v\d+/catalog/items", arg):

            embed = Embed(
                title="New link targeted",
                color=5763719,
                description=f"link {arg} now targeted to scrap",
                timestamp=datetime.now(timezone.utc)
            )

            await interaction.send_message(embed=embed)
            targeted_links.append(arg)
        else:
            await interaction.send_message(f"The link entered is invalid")
    else:
        await interaction.send_message("link already targeted")


bot.run(TOKEN)
