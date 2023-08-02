#################################################################################
#   ______ __                              ____________________________         #
#   ___  //_/___  _____________________ ______(_)__  __ )_  __ \__  __/         #
#   __  ,<  _  / / /_  ___/  __ \_  __ `__ \_  /__  __  |  / / /_  /            #
#   _  /| | / /_/ /_  /   / /_/ /  / / / / /  / _  /_/ // /_/ /_  /             #
#   /_/ |_| \__,_/ /_/    \____//_/ /_/ /_//_/  /_____/ \____/ /_/              #
#################################################################################
# Licensing: MPL-2.0                                                            #
# Author: @fiddlestix (opened-src)                                              #
# Credits: discord.py, stackoverflow, random                                    #
#################################################################################
# About KuromiBot: KuromiBot was a little side-project I made as a joke bot for #
# my friend group. I decided just because, I should open-source this project    #
# because I was bored and had nothing to do :p                                  #
#################################################################################

import os
import discord
import random
from discord import app_commands
from asyncio import sleep

# Setup ----------------------------------------------------------------------------------------------------------------------------


token = os.environ['TOKEN']
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Lists ----------------------------------------------------------------------------------------------------------------------------

eight_balls = ['yes',
               'maybe',
               'indeed',
               'fuck no',
               'nah',
               'dawg what the fuck?',
               'idk but im gay',
               'I hate you guys',
               'I would rather die than answer that question',
               'I guess',
               'ask your mother',
               'due to unfortunate circumcisions, I do not care enough to answer this question.',
               'my lawyers advised me against answering that question']

#TODO: Add more quotes
quotes_that_are_inspirational = ['bae I love it when your dicks on display',
                                 'ok',
                                 'Guys my butt hole is gaping and grape juice is spraying out',
                                 'CBT With Yuuka Kazami',
                                 'wtf why is the server icon siri on crack?']

talking_kuromi = ['Yes!',
                  'Hell no',
                  'Ugh',
                  '*Hangs up*',
                  'Hohoho'
                  'Hallo, Ich hieße Kuromi and german stuff.']

fun_facts = ['There is Hitler Rule34...',
             'Only one in every 1,000 sea turtles born make it to adulthood.',
             'When your skin burns and turns red due to sun exposure, it’s because your skin cells are killing themselves to avoid becoming cancerous.',
             'There is a rare and fatal condition in which the brain progressively destroys one’s ability to sleep.',
             'fun.',
             'Bananas are a little bit radioactive.',
             'The youngest person to ever give birth was Lina Medina, a Peruvian girl who gave birth to a child in 1939 at age five.',
             'There are brain-eating amoebas in freshwater ponds and lakes all over the world.',
             'Female ducks are so often forced into mating by male ducks that they have multiple vaginal defenses to confuse attackers and avoid unwanted pregnancies.',
             'The male honeybee exists only to mate with the queen bee, after which he is "castrated" and dies.',
             'There are only three states in America that have officially outlawed child marriage.',
             'There is a whale called 52 Blue that only sings at that frequency meaning it can’t communicate with other whales. It is nicknamed the loneliest whale on the planet.',
             'You might still be “it” from an unfinished game of tag',
             'Most animals will kill you before eating you, bears just start eating you',
             'According to quantum mechanics, there\'s a small chance the whole universe will suddenly disappear in the next 5 seconds',
             'When the gas chambers were first assembled and experimented with at the Auschwitz concentration camp, the SS soldiers that oversaw the process found that the people inside would start screaming as soon as the gas agent was dropped in. The screaming was so loud that it could be heard through the thick walls of the building, and the victims would continue screaming over the course of 20 minutes until it gradually faded to nothing. The screaming disturbed the soldiers (believe it or not), so they tried to think of a way to drown out the noise so they didn\'t have to hear it. Their idea was to get 2 motorcycles and rev the engines as loudly as they could at the same time during those 20 minutes. It didn\'t work.',
             'One day the last person who knows your name will die and you will be forgotten.',
             'Incest is legal in Maryland as long as it\'s only anal']

insults = ['stupid idiot',
           'loser',
           'you are a failure',
           'small dicked erectile dysfunction having dumbass',
           'gray sprinkle on a rainbow cupcake',
           'moronic fool',
           'are called a mistake, but God is perfect, so he made you to balance out the good looking people and the absolutely terrible looking people.',
           'your mom']

# Commands --------------------------------------------------------------------------------------------------------------------------


@tree.command(name="yes", description="No (uno reverse)")
async def ping(interaction):
    await interaction.response.send_message('no! {0}'.format(round(client.latency, 1)))


@tree.command(name="invite", description="Invite KuromiBot to your server.")
async def first_command(interaction):
    print(f"f[Command] Invite was ran!")
    await interaction.response.send_message("__**Add the bot!**__ <:Nice:1121512276680249425>\n__**https://discord.com/api/oauth2/authorize?client_id=1091835113530204240&permissions=105428298816&scope=bot**__\n\n*Maintained and developed by <@567854912004685844>*", ephemeral=True)


@tree.command(name="ask-me", description="Answers for all your questions! Like ChatGPT but better.")
async def question(interaction: discord.Interaction, anything: str):
    print(f"f[Command] ask-me was ran! Question: {question}")
    await interaction.response.send_message(f'{interaction.user.name} asked me {anything}? I say, {random.choice(eight_balls)}')


@tree.command(name="inspirational-quotes", description="Get a random inpirational quote.")
async def inspirationalquotes(interaction):
    print(f"[Command] inspirational-quotes was ran!")
    await interaction.response.send_message(random.choice(quotes_that_are_inspirational))


@tree.command(name="fun-facts", description="Fun facts!")
async def funfacts(interaction):
    print(f"[Command] fun-facts was ran!")
    await interaction.response.send_message(random.choice(fun_facts))


@tree.command(name="warn", description="Warn your friends and see if they unfriend you!")
async def warning(interaction: discord.Interaction, member: discord.Member, reason: str):
    await interaction.response.send_message(f" <a:warning:1126947077960765631> | Warned {member.mention} for {reason}, you {random.choice(insults)}")


@tree.command(name="talking-kuromi", description="Talking ben but objectively better.")
async def kuromi(interaction: discord.Interaction, question: str):
    await interaction.response.send_message(f'{question}\n {random.choice(talking_kuromi)}')


#Finalization--------------------------------------------------------------------------------------------------------------------------

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(client.guilds)} servers'))
        await sleep(120)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(client.users)} people... sweet dreams :)'))
        await sleep(120)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='everyone\'s bullshit'))
        await sleep(120)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name='Discord with Goomba\'s 8-ball'))
        await sleep(120)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with balls'))
        await sleep(120)


@client.event
async def on_ready():
    print("Ready!")
    await tree.sync()
    await client.loop.create_task(status())


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.guild:
        try:
            await message.channel.send("# Hello!\nI do not have the technical capability of reading or storing DMs, please join our support server if you need any help!\n**Support Server**: https://discord.gg/YwhFq69UhF")
        except discord.errors.Forbidden:
            pass
    else:
        pass


#Start the BOT--------------------------------------------------------------------------------------------------------------------------


client.run(token)
