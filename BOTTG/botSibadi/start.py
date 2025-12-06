import aiogram
import logging
import asyncio
from aiogram import F, Bot, Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, InputMediaPhoto
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
async def check_status(message: Message, state: FSMContext):
    ph_1 = InputMediaPhoto(type='photo',
                           media=FSInputFile('img/зачисление/зачисление1.png'))
    ph_2 = InputMediaPhoto(type='photo',
                           media=FSInputFile('img/зачисление/зачисление2.png'))
    ph_3 = InputMediaPhoto(type='photo',
                           media=FSInputFile('img/зачисление/зачисление3.png'))
    ph_4 = InputMediaPhoto(type='photo',
                           media=FSInputFile('img/зачисление/зачисление4.png'))

    zach_img = [
        ph_1, ph_2, ph_3, ph_4
    ]
    await message.answer(
        "1. Перейдите на сайт приемной комисии (https://sibadi.org/entrant/commission/)\n"
        "2. Выберите текущий год \n"
        "3. Выберите 'Если бы зачислениен было сегодня'\n"
        "4. Выберите нужную вам программу и форму обучения\n"
        "5. Выберите ваше направление\n"
        "6. По столбцу 'Уникальный код сервиса приема' найдите себя",
    )
    await message.answer_media_group(
        media = zach_img,
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
        "Для поступления в СибАДИ необходимы следующие документы:\n"
        "- документ, удостоверяющий личность \n"
        "- документ об образовании \n"
        "Дополнительно нужно предоставить: \n"
        "- СНИЛС\n"
        "- ИНН\n"
        "- Военный билет или приписное свидетельство (при наличии)\n"
        "Информацию о необходимых документах для поступления в 2025 году можно уточнить в приёмной комиссии СибАДИ",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "стоимость обучения")
async def documents(message: Message):
    await message.answer(
        "Стоимость обучения варьируется от 150.000 до 200.000 рублей за учебный курс \n"
        "Для подробной информации можно уточнить в приёмной комиссии",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "общежитие")
async def documents(message: Message):
    await message.answer(

        "В распоряжении университета 3 общежития: № 2, № 3, № 4 \n"
        "Стоимость варьируется от 700 до 2000 в зависимости от общежития и комнаты проживания \n"
        "Заселение происходит по договору с университетом. \n"
        "Необходимо предоставить документы, подтверждающие статус абитуриента (например, справка о подаче документов в вуз) \n"
        "Для уточнения деталей обращайтесь в администрацию общежитий или отдел по работе с учащимися СибАДИ.\n"
        "Или на сайте (https://sibadi.org/entrant/commission/priemnaya-komissiya-2025/)",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "как подать документы?")
async def documents(message: Message):
    await message.answer(
        "1. В Госулугах найдите вкладку 'Образование Дети'\n"
        "2. Далее нажмите на 'Поступление в вуз'\n"
        "3. Нажмите 'Подать заявление' \n"
        "4. Заполните всю необходимую информацию \n"
        "5. При выборе вуза найдите СибАДИ \n"
        "6. Выберите направления подготовки, на которые хотите поступить \n"
        "7. Проставьте приоритеты для выбранных направлений обучения \n"
        "8. Подтверите согласие с правилами предоставления услуги \n"
        "9. Отправьте заявление\n"
        "Для более подробной инструкции перейдите на сайт (https://www.gosuslugi.ru/vuzonline)",
        reply_markup=get_btn.faq_btns()
    )

@router.message(F.text.lower() == "график работы комиссии")
async def documents(message: Message):
    await message.answer(
        "Режим работы приемной комиссии:\n"
        "пн.-птн. с 9:00 до 17:45\n"
        "Перерыв на обед с 12:30  до 12:45 \n"
        "Суббота, Воскресенье-выходной",
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

