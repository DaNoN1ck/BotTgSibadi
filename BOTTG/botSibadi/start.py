import aiogram
import logging
import asyncio
from aiogram import F, Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums import ParseMode

import database
from config_reader import config
from aiogram.client.default import DefaultBotProperties
from aiogram import F
import get_btn
import sqlite3


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Добро пожаловать в СибАДИ, {message.from_user.full_name}\n"
        "Я помогу вам: \n"
        "\t - Узнать о направлениях\n"
        "\t - Получить консультацию",
        reply_markup= get_btn.menu_btn()
    )

@router.message(F.text.lower() == "главное меню")
async def menu(message: Message):
    await message.answer(
        "Чем могу помочь?", reply_markup=get_btn.show_menu()
    )

@router.message(F.text.lower() == "контакты")
async def contacts(message: Message):
    await message.answer(
        "Адрес \n"
        "г. Омск ул.Примерная, 1 \n"
        "Телефон: +7 (3812) 12-34-56 \n"
        "Email: primer@mail.ru \n"
        "Часы работы: \n"
        "Пн-Пт: 9:00-18-00\n"
        "Сб: 9:00-15-00",
        reply_markup=get_btn.menu_btn()
    )

@router.message(F.text.lower() == "проверить статус зачисления")
async def check_status(message: Message):
    await message.answer(
        "Переход на сайт с проверкой",
        reply_markup= get_btn.menu_btn()
    )


@router.message(F.text.lower() == "направление подготовки" or F.text.lower == "назад")
async def directions(message: Message):
    await message.answer(
        "Выберите направление ",
        reply_markup=get_btn.dir_btns()
    )

@router.message(F.text.lower() == "частые вопросы")
async def documents(message: Message):
    await message.answer(
        "Часто задаваемые вопросы ",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "какие документы нужны?")
async def documents(message: Message):
    await message.answer(
        "Ответ",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "стоимость обучения")
async def documents(message: Message):
    await message.answer(
        "Ответ",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "общежитие")
async def documents(message: Message):
    await message.answer(
        "Ответ",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "как подать документы?")
async def documents(message: Message):
    await message.answer(
        "Инструкция со скринами",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "график работы комиссии")
async def documents(message: Message):
    await message.answer(
        "Ответ",
        reply_markup=get_btn.faq_btns()
    )

@router.message()
async def programs(message: Message):
    text = message.text
    rows = database.get_db_direct()
    rowsProg = database.get_db_allprograms()
    rowsCond = database.get_db_conditions(text)
    rowsSubj = database.get_db_subjects(text)
    rowsEducations = database.get_db_education(text)
    for row in rows:
        for item in row:
            if(item == text):
                await message.answer(
                    "Выберите программу обучения",
                    reply_markup=get_btn.programs_btns(text)
                )
    for row in rowsProg:
        for item in row:
            if (item == text):
                await message.answer(
                    f"Выбранная программа:\n"
                    f"{text}\n"
                    f"Бюджетных мест: {rowsCond[0][1]}\n"
                    f"Платных мест: {rowsCond[0][2]}\n"
                    f"Проходной балл: {rowsCond[0][3]}\n"
                    f"Стоимость обучения: {rowsCond[0][4]} руб.\n"
                    f"Описание: {rowsCond[0][5]}\n"
                    f"Предметы ЕГЭ: {rowsSubj[0][1]}\n"
                    f"Профиль подготовки: {rowsEducations[0][1]}",
                    reply_markup=get_btn.dir_btns()
                )

