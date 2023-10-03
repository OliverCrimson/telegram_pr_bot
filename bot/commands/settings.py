from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .callback_data_states import CallbackSerialize


async def settings_cmd(message: Message) -> None:
    settings_markup = InlineKeyboardBuilder()
    settings_markup.button(
        text='Website', url='https://google.com'
    )
    settings_markup.button(text='Help', callback_data=CallbackSerialize(
        text='Hello buddy',
        user_id=message.from_user.id
    ))
    await message.answer(text='settings',
                         reply_markup=settings_markup.as_markup()
                         )


async def settings_callback(callback: CallbackQuery,
                            callback_data: CallbackSerialize
                            ):
    await callback.message.answer(
        f'{callback_data.text}, {str(callback_data.user_id)}'
    )
    await callback.answer()
