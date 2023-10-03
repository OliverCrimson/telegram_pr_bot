from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def start_cmd(message: Message) -> None:
    menu_build = ReplyKeyboardBuilder()
    menu_build.button(text='Help')
    menu_build.add(
        KeyboardButton(text='Send contact', request_contact=True)
    )
    menu_build.row(
        KeyboardButton(text='Send location', request_location=True),
        KeyboardButton(text='Send poll', request_poll=KeyboardButtonPollType())
    )
    await message.answer(text='Hello!',
                         reply_markup=menu_build.as_markup(
                             resize_keyboard=True)
                         )
