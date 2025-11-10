import aiogram
import logging
import asyncio
from aiogram import F, Bot,Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_reader import config
from aiogram.client.default import DefaultBotProperties
from aiogram import F


def show_menu() -> ReplyKeyboardMarkup:
    kb = [
        [
            types.KeyboardButton(text="Направление подготовки"),
            types.KeyboardButton(text="Частые вопросы"),
            types.KeyboardButton(text="Контакты"),
            types.KeyboardButton(text="Поддержка")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard

def back_menu_btns() -> ReplyKeyboardMarkup:
    kb = [
        [
            types.KeyboardButton(text = "Вернуться"),
            types.KeyboardButton(text = "Главное меню")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard

def menu_btn ()-> ReplyKeyboardMarkup:
    kb = [
        [
            types.KeyboardButton(text="Главное меню")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard

def faq_btns() -> ReplyKeyboardMarkup:

    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text = "Какие документы нужны?"))
    builder.add(types.KeyboardButton(text="Стоимость обучения"))
    builder.add(types.KeyboardButton(text="Общежитие"))
    builder.add(types.KeyboardButton(text="Вступительные испытания"))
    builder.add(types.KeyboardButton(text="График работы комиссии"))
    builder.add(types.KeyboardButton(text="Главное меню"))
    builder.adjust(3)
    return builder.as_markup(resize_keyboard = True)