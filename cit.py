import discord
import os
from discord.ext import 
from keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

GIF_URL = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2luZm9ieTI5YTFhaDE4d3dqdDZpcW1uYWhhN2h6MnFhcHNoM2lqZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YZX4FWwOJTK5W/giphy.gif"

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="👋chào-mừng")
    if channel:
        
        await channel.send(f"**✨ CHÀO MỪNG CON VỢ {member.mention} ✨**\nChúc con vợ có một khoảng thời gian đẹp trong server này 💖")
        
        await channel.send(GIF_URL)
keep_alive()
bot.run(TOKEN)
