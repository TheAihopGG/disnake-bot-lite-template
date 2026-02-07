from disnake.ext.commands import Cog, InteractionBot


class MyCog(Cog):
    def __init__(self, bot: InteractionBot):
        self.bot = bot


def setup(bot: InteractionBot):
    bot.add_cog(MyCog(bot=bot))
