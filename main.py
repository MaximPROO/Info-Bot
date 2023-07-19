from aiogram import Dispatcher, Bot, types, executor
import requests, datetime
from random import choice
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
bot = Bot(token="") # Insert token

dp = Dispatcher(bot=bot)

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Получить цитату 💌"),
            KeyboardButton("Есть ли сегодня праздник ❓")
        ],
        [
            KeyboardButton('Информация обо мне 🙋‍♂️'),
            KeyboardButton("Что умеет этот бот 🤖")
        ],
        [
            KeyboardButton("О создателе бота ✔")
        ]
    ], resize_keyboard=True
)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f"Ассаляму алейкум {message.from_user.full_name.title()}👋\n"
                         "Добро пожаловать в бота!\n"
                         "Информацию о боте вы можете получить ниже ⬇", reply_markup=start_keyboard)

@dp.message_handler(text="Получить цитату 💌")
async def cmd_send_quota(message: types.Message):
    quota = requests.get("https://favqs.com/api/qotd").json()
    # quota = quota['quote']['body']

    await message.answer(f"Сгенерирована цитата, теги {','.join(quota['quote']['tags'])}\n"
                         f"Содержиме {quota['quote']['body']}\n"
                         "Author <a href='https://t.me/maximPRO0'>Максим Орлов</a>",
                         parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)

@dp.message_handler(text="Есть ли сегодня праздник ❓")
async def cmd_holidats(message: types.Message):
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day

    api_key = "" # Enter you token  calendarific.com
    holiday = requests.get(f'https://calendarific.com/api/v2/holidays?api_key={api_key}&country=UZ&year={year}&month={month}&day={day}').json()
    holiday = holiday['response']['holidays']
    if holiday:
        await message.answer(f"В республике Узбекистан сегодня праздник {holiday}")
    else:
        await message.answer("Увы, но сегодня вы без праздника☹")


@dp.message_handler(text="Информация обо мне 🙋‍♂️")
async def cmd_userinfo(message: types.Message):
    replics = ['Плохой',"Хороший","Ужасный", "Просто мразь", "Простая тема", "Онглечанен", "Реппер", "Прараб", "Разраб"]
    await message.answer("Что знает о вас этот бот ?\n"
                         f"🔹Вы {message.from_user.full_name.title()}🎩\n"
                         f"🔹Ваш ID: {message.from_user.id}🆔\n"
                         f"🔹Ваш username {message.from_user.username}☣️\n"
                         f"🔹А еще вы {choice(replics)}")
    

@dp.message_handler(text="Что умеет этот бот 🤖")
async def cmd_bots_commands(message: types.Message):
    await message.answer("Не будем сильно вдовать в подробности\n"
                         "Пока что для тебя я просто обычный бот"
                         "А многого тебе знать не надо, просто знай что тут есть жизнь")
    
@dp.message_handler(text="О создателе бота ✔")
async def cmd_owner(message: types.Message):
    if message.from_user.id == 5136115153:
        await message.answer("Ты что теперь будеш каждые две минуты о себе инфу проверять!?")
    else:
        await message.answer("И так, самое интересное, о создателе\n"
                             "На самом деле очень конфидеациальная информация🤫\n"
                             "И на на личные данные переходить не будем\n"
                             f"Орлов Максим, так разработчик себя называет\n"
                             "В 19 лет Team leader в MRIT\n"
                             "Concatc: (91)523-81-66 📞\n"
                             "Email: maximpro0@bk.ru 📩", disable_web_page_preview=True)
        


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
