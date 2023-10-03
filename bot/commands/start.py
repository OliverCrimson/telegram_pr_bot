from aiogram.types import Message


async def start_cmd(message: Message) -> None:
    await message.answer(text='Hello!')
