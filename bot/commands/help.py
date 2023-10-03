from aiogram.filters import CommandObject
from aiogram.types import Message

from bot.commands.bot_commands import bot_commands


async def help_command(message: Message, command: CommandObject) -> Message:
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
                )
            else:
                return await message.answer("Command not found")
    else:
        return await message.answer(
            'Help with bot\n'
            'Use /help if help is needed.'
        )
