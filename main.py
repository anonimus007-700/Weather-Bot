from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

today = date.today()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('/weather - погода')

@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    await message.answer('Вибери місто, або введи своє', reply_markup=kb.weather_button)

@dp.message_handler()
async def weather_msg(message: types.Message):
    await message.reply("На коли?", reply_markup=kb.inline_kb)
    global f
    f = message.text
    
@dp.callback_query_handler(lambda call:True)
async def weathers(call):
    def wind():
        div = soup.find_all("div", attrs={'class': 'wind'})
        for i in div:
            b = i.attrs['data-tooltip']
            winds.append(b)  
    def wea():
        for link in tabs:
            wi = link.find(class_="weatherIco").get("title")
            day_link = link.find(class_="day-link").text
            date = link.find(class_="date").text
            month = link.find(class_="month").text
            min = link.find(class_="min").text
            max = link.find(class_="max").text
            bonu=f"{day_link}{'_'}{date}{'_'}{month}{'_'}{wi}{'_'}{min}{'_'}{max}"
            quote.append(bonu)
        for row in soup.select('tbody tr'):
            row_text = [x.text for x in row.find_all('td')]
            detal.append(row_text)
    
    if call.data == 'today':
        quote, out, detal, winds = [], [], [], []
        
        url = f'https://ua.sinoptik.ua/погода-{f}'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        tabs = soup.find(class_="tabs").find_all(class_="main")
    
        wea()
        wind()
        
        a1 = quote[0].split('_')
        for i in a1:
            out.append(i)
            a1 = '\n'.join(out)
        await bot.send_message(call.message.chat.id, a1)
                
    elif call.data == 'tomorrow':
        quote, out, detal, winds = [], [], [], []
        tomorrow = today + timedelta(days=1)
        
        url = f'https://ua.sinoptik.ua/погода-{f}/{tomorrow}'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        tabs = soup.find(class_="tabs").find_all(class_="main")
    
        wea()
        wind()
        
        a2 = quote[1].split('_')
        for i in a2:
            out.append(i)
            a2 = '\n'.join(out)
        await bot.send_message(call.message.chat.id, a2)

    night_text = text(
        'Ніч\n',
        f'{detal[0][0]} | {detal[0][1]}\n\n',
        "Температура, °C:\n",
        detal[2][0],
        '  |  ',
        detal[2][1],
        "\n\nВітер:\n",
        winds[0],
        '  |  ',
        winds[1],
        "\n\nЙмовірність опадів, %:\n",
        detal[7][0],
        '  |  ',
        detal[7][1]
    )
    morning_text = text(
        'Ранок\n',
        f'{detal[0][2]} | {detal[0][3]}\n\n',
        "Температура, °C:\n",
        detal[2][2],
        '  |  ',
        detal[2][3],
        "\n\nВітер:\n",
        winds[2],
        '  |  ',
        winds[3],
        "\n\nЙмовірність опадів, %:\n",
        detal[7][2],
        '  |  ',
        detal[7][3]
    )
    day_text = text(
        'День\n',
        f'{detal[0][4]} | {detal[0][5]}\n\n',
        "Температура, °C:\n",
        detal[2][4],
        '  |  ',
        detal[2][5],
        "\n\nВітер:\n",
        winds[4],
        '  |  ',
        winds[5],
        "\n\nЙмовірність опадів, %:\n",
        detal[7][4],
        '  |  ',
        detal[7][5]
    )
    night2_text = text(
        'Вечір\n',
        f'{detal[0][6]} | {detal[0][7]}\n\n',
        "Температура, °C:\n",
        detal[2][6],
        '  |  ',
        detal[2][7],
        "\n\nВітер:\n",
        winds[6],
        '  |  ',
        winds[7],
        "\n\nЙмовірність опадів, %:\n",
        detal[7][6],
        '  |  ',
        detal[7][7]
        
    )
        
    await bot.send_message(call.message.chat.id, night_text)
    await bot.send_message(call.message.chat.id, morning_text)
    await bot.send_message(call.message.chat.id, day_text)
    await bot.send_message(call.message.chat.id, night2_text)
    
    print('[bot]', f)

        
if __name__ == '__main__':
    executor.start_polling(dp)
