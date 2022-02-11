from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_paginate_keyboard(next_page: str = None, previous_page: str = None) -> InlineKeyboardMarkup:
    """
    Function return inline keyboard with paginate.
    """
    next_page = next_page.split('p=')[1] if next_page else '❌'
    if previous_page:
        previous_page = '1' if previous_page.endswith('/users/') else previous_page.split('p=')[1]
    else:
        previous_page = '❌'

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{previous_page}', callback_data=f'page={previous_page}'),
                InlineKeyboardButton(text='EXIT', callback_data='exit'),
                InlineKeyboardButton(text=f'{next_page}', callback_data=f'page={next_page}')
            ],
        ])
    return keyboard


async def get_exit_keyboard() -> InlineKeyboardMarkup:
    """
    Function return keyboard that using for exit from any state.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='EXIT', callback_data='exit')]])
    return keyboard
