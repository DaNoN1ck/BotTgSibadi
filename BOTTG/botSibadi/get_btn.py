import aiogram
import logging
import asyncio
from aiogram import F, Bot,Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import os
import pandas as pd
import sqlite3

import database
from config_reader import config
from aiogram.client.default import DefaultBotProperties
from aiogram import F




def dir_btns() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    rows = database.get_db_direct()
    builder.add(types.KeyboardButton(text = "Главное меню"))
    for row in rows:
        builder.add(types.KeyboardButton(text=str(row[1])))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)



def show_menu() -> ReplyKeyboardMarkup:
    kb = [
        [
            types.KeyboardButton(text="Проверить статус зачисления"),
            types.KeyboardButton(text="Направление подготовки"),
            types.KeyboardButton(text="Частые вопросы"),
            types.KeyboardButton(text="Контакты"),

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
    builder.add(types.KeyboardButton(text="Как подать документы?"))
    builder.add(types.KeyboardButton(text="График работы комиссии"))
    builder.add(types.KeyboardButton(text="Главное меню"))
    builder.adjust(3)
    return builder.as_markup(resize_keyboard = True)

def programs_btns(direct) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    rows = database.get_db_programs(direct)
    builder.add(types.KeyboardButton(text="Главное меню"))
    for row in rows:
        builder.add(types.KeyboardButton(text=str(row[1])))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard = True)

def conditions_btns() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Главное меню"))
    builder.add(types.KeyboardButton(text="Назад"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard = True)