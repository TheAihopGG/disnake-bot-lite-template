from disnake.ext.commands import InteractionBot
from logging import getLogger

from core.config import BOT_TOKEN
from core.logging import configure_logging

configure_logging()

logger = getLogger()
bot = InteractionBot(sync_commands_debug=True)
bot.load_extensions("cogs")


@bot.event
async def on_ready():
    logger.info("Бот успешно запущен")


bot.run(BOT_TOKEN)
