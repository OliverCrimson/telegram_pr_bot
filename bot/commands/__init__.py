__all__ = ['register_user_cmds', 'bot_commands']

from aiogram.filters import Command, CommandStart
from aiogram import Router, F

from .callback_data_states import CallbackSerialize
from .start import start_cmd
from bot.commands.help import help_command, help_func, callback_help
from bot.commands.settings import settings_cmd, settings_callback


def register_user_cmds(router: Router) -> None:
    router.message.register(start_cmd, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(help_func, F.text == 'Help')
    router.message.register(settings_cmd, Command(commands=['settings']))
    router.callback_query.register(callback_help, F.data == 'help')
    router.callback_query.register(settings_callback,
                                   CallbackSerialize.filter())
