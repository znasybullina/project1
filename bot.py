import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from keyboard import get_main_keyboard

from keyboard import get_second_keyboard
from schedule_handler import get_main_schedule_for_day, get_extra_schedule_for_day

API_TOKEN = "8356198781:AAGW8J8kjQ4dBox4PI2XJJd6-xOmBa9vNV8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

current_class = dict()


async def main():
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "Здравствуйте, расписание какого класса вы хотите посмотреть?",
        reply_markup=get_main_keyboard()
    )


classes = ["7А", "7Б", "8А", "8Б", "9А", "9Б", "10А", "10Б", "11А", "11Б"]


@dp.message(F.text.in_(classes))
async def handle_class_selection(message: Message):
    global current_class
    selected_class = message.text
    current_class[message.from_user.id] = message.text
    response = f"Вы выбрали {selected_class} класс"

    logging.info(f"Пользователь {message.from_user.id} выбрал {selected_class}")
    await message.answer(response, reply_markup=get_second_keyboard())


weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]


@dp.message(F.text.in_(weekdays))
async def handle_weekday_selection(message: Message):
    selected_weekday = message.text
    logging.info(f"Пользователь {message.from_user.id} выбрал {selected_weekday}")

    main_schedule = get_main_schedule_for_day(selected_weekday, current_class[message.from_user.id])
    response = "*Основное расписание:*\n"
    for index, lesson in enumerate(main_schedule):
        response += f"{index + 1}) {lesson}\n"

    response += "\n*Дополнительные занятия:*\n"
    extra_schedule = get_extra_schedule_for_day(selected_weekday, current_class[message.from_user.id])
    for index, lesson in enumerate(extra_schedule):
        response += f"{index + 1}) {lesson}\n"

    await message.answer(
        text=response,
        parse_mode=ParseMode.MARKDOWN
    )


@dp.message(F.text.in_("Назад ↩️"))
async def handle_back_button(message: Message):
    global current_class
    current_class[message.from_user.id] = None
    await message.answer(
        "Расписание какого класса вы хотите посмотреть?",
        reply_markup=get_main_keyboard()
    )


if __name__ == "__main__":
    asyncio.run(main())
