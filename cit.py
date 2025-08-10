import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

GIF_URL = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbndndGNiYnl6bThwcmVzMnRqcHA1OTAyMm1ydnEzc284NDluMG1xMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g5J6pilmOCoSL1nRRk/giphy.gif"

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
