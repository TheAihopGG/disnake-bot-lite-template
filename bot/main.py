from disnake.ext.commands import InteractionBot, CommandSyncFlags
from logging import getLogger

from core.config import BOT_TOKEN
from core.logging import configure_logging

configure_logging()

logger = getLogger()
bot = InteractionBot(command_sync_flags=CommandSyncFlags(sync_commands_debug=True))
bot.load_extensions("cogs")


@bot.event
async def on_ready():
    logger.info("Бот успешно запущен")


bot.run(BOT_TOKEN)
