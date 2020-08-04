import telebot
import requests

token = "1028814748:AAGxNeS3k3V4OvHNsw-xxXViXjxcqcju4vw"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def say_hello(message):
    msg = 'Курс валют - /Valute\nПогода - /Weather'
    print(message)
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=["Valute"])
def get_valute(message):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    currency = requests.get(url).json()
    #print(currency["Valute"])
    usd = currency["Valute"]["USD"]["Value"]
    eur = currency["Valute"]["EUR"]["Value"]
    bot.send_message(message.chat.id, f"Доллар: {usd}, Евро: {eur}")

@bot.message_handler(commands=["Weather"])
def get_city(message):
    msg = bot.send_message(message.chat.id,"Укажите, пожалуйста, ваш город")
    bot.register_next_step_handler(msg, get_weather)

def get_weather(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c476f22a5b257b9d84b96dbf18ad854"
    data = requests.get(url).json()
    bot.send_message(message.chat.id, f"{city} - {(data['main']['temp'] - 273.15) //1} °Цельсия")
    
bot.polling()
