import os
import pandas as pd
import sqlite3
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


conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

def clean_text(text):
    return text.strip("(),'")


def get_db_direct():
    cursor.execute("SELECT * FROM directions")
    rows = cursor.fetchall()
    return rows

def get_db_programs(direct):
    cursor.execute("SELECT a.* FROM programs a LEFT JOIN directions b ON a.id_direct = b.id_direct WHERE b.title = ?", (direct,))
    rows = cursor.fetchall()
    return rows

def get_db_allprograms():
    cursor.execute("SELECT a.title_prog FROM programs a LEFT JOIN directions b ON a.id_direct = b.id_direct")
    rows = cursor.fetchall()
    return rows


def get_db_conditions(program):
    cursor.execute("SELECT a.* FROM conditions a LEFT JOIN programs b ON a.id_prog = b.id_prog WHERE b.title_prog = ?",
                   (program,))
    rows = cursor.fetchall()
    return rows


def get_db_allconditions():
    cursor.execute("SELECT a.* FROM conditions a LEFT JOIN programs b ON a.id_prog = b.id_prog")
    rows = cursor.fetchall()
    return rows

def get_db_subjects(title_prog):
    cursor.execute("SELECT a.* FROM subjects a LEFT JOIN conditions b LEFT JOIN programs c ON a.id_subject = b.id_subject AND c.id_prog = b.id_prog   WHERE c.title_prog = ?", (title_prog,))
    rows = cursor.fetchall()
    return rows

def get_db_education(title_prog):
    cursor.execute("SELECT a.* FROM educations a LEFT JOIN conditions b LEFT JOIN programs c ON a.id_education = b.id_education AND c.id_prog = b.id_prog WHERE c.title_prog = ?", (title_prog,))
    rows = cursor.fetchall()
    return rows

rows = get_db_subjects("Стратегическое управление логистикой")
print(rows[0][1])