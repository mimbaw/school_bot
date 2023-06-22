import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import MessageNotModified

from config import BOT_TOKEN
from data import data

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)



def get_back_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Назад", callback_data="back")
    kb.add(button_1)
     
    return kb

def get_classes_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("5", callback_data="get_5_class")
    button_2 = InlineKeyboardButton("6", callback_data="get_6_class")
    button_3 = InlineKeyboardButton("7", callback_data="get_7_class")
    button_4 = InlineKeyboardButton("8", callback_data="get_8_class")
    button_5 = InlineKeyboardButton("9", callback_data="get_9_class")
    button_6 = InlineKeyboardButton("10", callback_data="get_10_class")
    button_7 = InlineKeyboardButton("11", callback_data="get_11_class")
    kb.add(button_1, button_2, button_3)
    kb.add(button_4, button_5, button_6)
    kb.add(button_7)
     
    return kb


def get_5_class_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Натуральные числа и нуль", callback_data="5_Натуральные числа и нуль")
    button_2 = InlineKeyboardButton("Дроби", callback_data="5_Дроби")
    button_3 = InlineKeyboardButton("Решение текстовых задач", callback_data="5_Решение текстовых задач")
    button_4 = InlineKeyboardButton("Наглядная геометрия", callback_data="5_Наглядная геометрия")
    button_5 = InlineKeyboardButton("Назад", callback_data="back")
    kb.add(button_1, button_2)
    kb.add(button_3, button_4)
    kb.add(button_5)

    return kb
    

def get_6_class_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Дроби", callback_data="6_Дроби")
    button_2 = InlineKeyboardButton("Натуральные числа", callback_data="6_Натуральные числа")
    button_3 = InlineKeyboardButton("Наглядная геометрия", callback_data="6_Наглядная геометрия")
    button_4 = InlineKeyboardButton("Буквенные выражения", callback_data="6_Буквенные выражения")
    button_5 = InlineKeyboardButton("Решение текстовых задач", callback_data="6_Решение текстовых задач")
    button_6 = InlineKeyboardButton("Положительные и отрицательные числа", callback_data="6_Положительные и отрицательные")
    button_7 = InlineKeyboardButton("Назад", callback_data="back")

    kb.add(button_1)
    kb.add(button_2)
    kb.add(button_3)
    kb.add(button_4)
    kb.add(button_5)
    kb.add(button_6)
    kb.add(button_7)

    return kb


def get_7_class_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Уравнения", callback_data="7_Уравнения")
    button_2 = InlineKeyboardButton("Рациональные числа", callback_data="7_Рациональные числа")
    button_3 = InlineKeyboardButton("Алгебраические выражения", callback_data="7_Алгебраические выражения")
    button_4 = InlineKeyboardButton("Координаты и графики. Функции", callback_data="7_Координаты и графики. Функции")
    button_5 = InlineKeyboardButton("Назад", callback_data="back")
    kb.add(button_1)
    kb.add(button_2)
    kb.add(button_3)
    kb.add(button_4)
    kb.add(button_5)

    return kb


def get_8_class_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Функции", callback_data="8_Функции")
    button_2 = InlineKeyboardButton("Уравнения и неравенства", callback_data="8_Уравнения и неравенства")
    button_3 = InlineKeyboardButton("Алгебраические выражения", callback_data="8_Алгебраические выражения")
    button_4 = InlineKeyboardButton("Числа и вычисления. Работа с корнями", callback_data="8_Числа и вычисления. Работа")
    button_5 = InlineKeyboardButton("Назад", callback_data="back")
    kb.add(button_1)
    kb.add(button_2)
    kb.add(button_3)
    kb.add(button_4)
    kb.add(button_5)

    return kb


def get_9_class_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Арифметическая и геометрическая прогрессии", callback_data="9_Арифметическая и геометрическая")
    button_2 = InlineKeyboardButton("Измерения, приближения, оценки", callback_data="9_Измерения, приближения, оценки")
    button_3 = InlineKeyboardButton("Уравнения с одной переменной", callback_data="9_Уравнения с одной переменной")
    button_4 = InlineKeyboardButton("Системы уравнений", callback_data="9_Системы уравнений")
    button_5 = InlineKeyboardButton("Системы неравенств", callback_data="9_Системы неравенств")
    button_6 = InlineKeyboardButton("Функции", callback_data="9_Функции")
    button_7 = InlineKeyboardButton("Числовые последовательности", callback_data="9_Числовые последовательности")
    button_8 = InlineKeyboardButton("Действительные числа", callback_data="9_Действительные числа")
    button_9 = InlineKeyboardButton("Назад", callback_data="back")
    kb.add(button_1)
    kb.add(button_2)
    kb.add(button_3, button_4)
    kb.add(button_5, button_6)
    kb.add(button_7, button_8)
    kb.add(button_9)

    return kb


def get_10_class_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Делимость чисел", callback_data="10_Делимость чисел")
    button_2 = InlineKeyboardButton("Степенная функция", callback_data="10_Степенная функция")
    button_3 = InlineKeyboardButton("Показательная функция", callback_data="10_Показательная функция")
    button_4 = InlineKeyboardButton("Логарифмическая функция", callback_data="10_Логарифмическая функция")
    button_5 = InlineKeyboardButton("Тригонометрические уравнения", callback_data="10_Тригонометрические уравнения")
    button_6 = InlineKeyboardButton("Степень с действительным показателем", callback_data="10_Степень с действительным")
    button_7 = InlineKeyboardButton("Многочлены. Алгебраические уравнения", callback_data="10_Многочлены. Алгебраические")
    button_8 = InlineKeyboardButton("Тригонометрические выражения и их преобразование", callback_data="10_Тригонометрические выражения")
    button_9 = InlineKeyboardButton("Назад", callback_data="back")
    kb.add(button_1)
    kb.add(button_2)
    kb.add(button_3)
    kb.add(button_4)
    kb.add(button_5)
    kb.add(button_6)
    kb.add(button_7)
    kb.add(button_8)
    kb.add(button_9)

    return kb


def get_11_class_kb():
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Тригонометрические функции", callback_data="11_Тригонометрические функции")
    button_2 = InlineKeyboardButton("Производная и её геометрический смысл", callback_data="11_Производная и её геометрический")
    button_3 = InlineKeyboardButton("Первообразная и интеграл", callback_data="11_Первообразная и интеграл")
    button_4 = InlineKeyboardButton("Уравнения и неравенства с двумя переменными", callback_data="11_Уравнения и неравенства")
    button_5 = InlineKeyboardButton("Элементы теории вероятностей", callback_data="11_Элементы теории вероятностей")
    button_6 = InlineKeyboardButton("Комбинаторика", callback_data="11_Комбинаторика")
    button_7 = InlineKeyboardButton("Комплексные числа", callback_data="11_Комплексные числа")
    button_8 = InlineKeyboardButton("Назад", callback_data="back")
    kb.add(button_1)
    kb.add(button_2)
    kb.add(button_3)
    kb.add(button_4)
    kb.add(button_5)
    kb.add(button_6, button_7)
    kb.add(button_8)

    return kb


@dp.message_handler(commands=["start"])
async def message_handler(message: Message):
    await message.answer("Выберите класс", reply_markup=get_classes_kb())


@dp.callback_query_handler()
async def callback_handler(call: CallbackQuery):
    try:
        if call.data == "get_5_class":
            await call.message.edit_text("Выберите тему", reply_markup=get_5_class_kb())
        elif call.data == "get_6_class":
            await call.message.edit_text("Выберите тему", reply_markup=get_6_class_kb())
        elif call.data == "get_7_class":
            await call.message.edit_text("Выберите тему", reply_markup=get_7_class_kb())
        elif call.data == "get_8_class":
            await call.message.edit_text("Выберите тему", reply_markup=get_8_class_kb())
        elif call.data == "get_9_class":
            await call.message.edit_text("Выберите тему", reply_markup=get_9_class_kb())
        elif call.data == "get_10_class":
            await call.message.edit_text("Выберите тему", reply_markup=get_10_class_kb())
        elif call.data == "get_11_class":
            await call.message.edit_text("Выберите тему", reply_markup=get_11_class_kb())

        elif call.data == "back":
            await call.message.edit_text("Выберите класс", reply_markup=get_classes_kb())

        else:
            a_class = call.data.split('_')[0]
            course = call.data.split('_')[-1]
            await call.message.edit_text(f"Ваш материал:\n{data[a_class][course]}", reply_markup=get_back_kb())
    except MessageNotModified:
        return


if __name__ == "__main__":
    executor.start_polling(dp)