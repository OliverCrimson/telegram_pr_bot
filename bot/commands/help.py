from aiogram.filters import CommandObject
from aiogram.types import Message, CallbackQuery

from .bot_commands import bot_commands_tuple as coms


async def help_command(message: Message, command: CommandObject):
    if command.args:
        for cmd in coms:
            if cmd[0] == command.args:
                return await message.answer(
                    f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
                )
            else:
                return await message.answer("Command not found")
    return await help_func(message)


async def help_func(message: Message) -> Message:
    return await message.answer(
        'Help with bot\n'
        'Use /help if help is needed.'
    )


async def callback_help(callback: CallbackQuery):
    await callback.message.edit_text(
        'Hi from callback',
        reply_markup=callback.message.reply_markup
    )
    await callback.answer()
