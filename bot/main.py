import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from dotenv import load_dotenv

from commands import register_user_cmds, bot_commands

load_dotenv()


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    bot_commands_list = []
    for cmd in bot_commands:
        bot_commands_list.append(BotCommand(
            command=cmd[0],
            description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=os.getenv("TG_API_TOKEN"))
    await bot.set_my_commands(commands=bot_commands_list)
    register_user_cmds(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Stopped')
