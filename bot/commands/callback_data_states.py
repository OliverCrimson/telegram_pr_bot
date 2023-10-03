from aiogram.filters.callback_data import CallbackData


class CallbackSerialize(CallbackData, prefix='test'):
    text: str
    user_id: int
