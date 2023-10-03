__all__ = ['register_user_cmds', 'bot_commands']

from aiogram.filters import Command, CommandStart
from aiogram import Router
from .start import start_cmd
from bot.commands.help import help_command


bot_commands = (
    ("start", "Start bot", "Type /start to run the bot"),
    ("help", "Help", "If it is necessary"),

)


def register_user_cmds(router: Router) -> None:
    router.message.register(start_cmd, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
