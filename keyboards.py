from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

today = InlineKeyboardButton('Сьогодні', callback_data='today')
tomorrow = InlineKeyboardButton('Завтра', callback_data='tomorrow')
inline_kb = InlineKeyboardMarkup().add(today, tomorrow)

city1 = KeyboardButton('Сімферополь')
city2 = KeyboardButton('Вінниця')
city3 = KeyboardButton('Луцьк')
city4 = KeyboardButton('Дніпро')
city5 = KeyboardButton('Донецьк')
city6 = KeyboardButton('Житомир')
city7 = KeyboardButton('Ужгород')
city8 = KeyboardButton('Запоріжжя')
city9 = KeyboardButton('Івано-Франківськ')
city10 = KeyboardButton('Київ')
city11 = KeyboardButton('Кропивницький')
city12 = KeyboardButton('Луганськ')
city13 = KeyboardButton('Львів')
city14 = KeyboardButton('Миколаїв')
city15 = KeyboardButton('Одеса')
city16 = KeyboardButton('Полтава')
city17 = KeyboardButton('Рівне')
city18 = KeyboardButton('Суми')
city19 = KeyboardButton('Тернопіль')
city20 = KeyboardButton('Харків')
city21 = KeyboardButton('Херсон')
city22 = KeyboardButton('Хмельницький')
city23 = KeyboardButton('Черкаси')
city24 = KeyboardButton('Чернівці')
city25 = KeyboardButton('Чернігів')
city26 = KeyboardButton('Севастополь')
weather_button = ReplyKeyboardMarkup(resize_keyboard=True).add(city1,city2,city3,city4,city5,city6,
                                                               city7,city8,city9,city10,city11,city12,
                                                               city13,city14,city15,city16,city17,city18,
                                                               city19,city20,city21,city22,city23,city24,
                                                               city25, city26)
