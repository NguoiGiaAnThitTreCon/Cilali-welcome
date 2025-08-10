import discord
import os
import random
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

GIF_URL = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbndndGNiYnl6bThwcmVzMnRqcHA1OTAyMm1ydnEzc284NDluMG1xMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g5J6pilmOCoSL1nRRk/giphy.gif"

# Danh sách câu thả thính
THA_THINH_LIST = [
    "Muốn đẻ con cho anh @trong_65 quá",
    "Anh @trong_65 ơi, em yêu anh mất rồi 🥰",
    "Làm vợ anh @trong_65 chắc hạnh phúc lắm",
    "Anh @trong_65 cười là tim em tan chảy",
    "Có thể cho em họp phụ huynh với mẹ anh @trong_65 không 😳",
    "Em xin phép được nắm tay anh @trong_65 trọn đời",
    "Nhìn anh @trong_65 thôi cũng đủ no",
    "Anh @trong_65 là chân ái của đời em",
    "Em muốn bên anh @trong_65 cả kiếp này"
]

async def change_status_loop():
    await bot.wait_until_ready()
    while not bot.is_closed():
        status_text = random.choice(THA_THINH_LIST)
        activity = discord.Game(name=status_text)
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(30)  # 30 giây đổi một lần

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập: {bot.user}")
    asyncio.create_task(change_status_loop())

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="👋chào-mừng")
    if channel:
        await channel.send(f"**✨ CHÀO MỪNG CON VỢ {member.mention} ✨**\nChúc con vợ có một khoảng thời gian đẹp trong server này 💖")
        await channel.send(GIF_URL)

keep_alive()
bot.run(TOKEN)
