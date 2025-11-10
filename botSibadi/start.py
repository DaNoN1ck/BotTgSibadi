import aiogram
import logging
import asyncio
from aiogram import F, Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums import ParseMode
from config_reader import config
from aiogram.client.default import DefaultBotProperties
from aiogram import F
import get_btn

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

@router.message(F.text.lower() == "вступительные испытания")
async def documents(message: Message):
    await message.answer(
        "Ответ",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "график работы комиссии")
async def documents(message: Message):
    await message.answer(
        "Ответ",
        reply_markup=get_btn.faq_btns()
    )

