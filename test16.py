import requests
import json
 
url = 'http://t1.polygon.ru'
json_url = 'http://t1.polygon.ru'
session = requests.Session()
r = session.get(url)
if r.status_code == 200:
  json_r = session.get(json_url)
  if json_r.status_code == 200:
    data = json.loads(json_r.text)
    znacheniya1 = data["variables"]["temperature"], data["variables"]["humidity"]
    print(znacheniya1)
  else:
    print(json_r.status_code)
 
##########################################################################################################
url = 'http://t2.polygon.ru'
json_url = 'http://t2.polygon.ru'
session = requests.Session()
r = session.get(url)
if r.status_code == 200:
  json_r = session.get(json_url)
  if json_r.status_code == 200:
    data = json.loads(json_r.text)
    znacheniya2 = data["variables"]["temperature"], data["variables"]["humidity"]
    print(znacheniya2)
  else:
    print(json_r.status_code)
#####################################################################################################################################
url = 'http://t3.polygon.ru'
json_url = 'http://t3.polygon.ru'
session = requests.Session()
r = session.get(url)
if r.status_code == 200:
  json_r = session.get(json_url)
  if json_r.status_code == 200:
    data = json.loads(json_r.text)
    znacheniya3 = data["variables"]["temperature"], data["variables"]["humidity"]
    print(znacheniya3)
  else:
    print(json_r.status_code)
###########################################################################################################################################
url = 'http://t4.polygon.ru'
json_url = 'http://t4.polygon.ru'
session = requests.Session()
r = session.get(url)
if r.status_code == 200:
  json_r = session.get(json_url)
  if json_r.status_code == 200:
    data = json.loads(json_r.text)
    znacheniya4 = data["variables"]["temperature"], data["variables"]["humidity"]
    print(znacheniya4)
  else:
    print(json_r.status_code)
#################################################################################################################################
url = 'http://t5.polygon.ru'
json_url = 'http://t5.polygon.ru'
session = requests.Session()
r = session.get(url)
if r.status_code == 200:
  json_r = session.get(json_url)
  if json_r.status_code == 200:
    data = json.loads(json_r.text)
    znacheniya5 = data["variables"]["temperature"], data["variables"]["humidity"]
    print(znacheniya5)
  else:
    print(json_r.status_code)


 
import telebot
bot = telebot.TeleBot('5144383160:AAHlK_6erszNTDyA-Eg_kkHFdeaRkiJtWAE');
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, тут ты можешь узнать информацию о микроклимате в полигоне. Введи /help")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Выбери кабинет: /430 /429 /428 /427 /425")
  elif message.text == "/430":
      bot.send_message(message.from_user.id, znacheniya1)
  elif message.text == "/429":
      bot.send_message(message.from_user.id, "znacheniya2")
  elif message.text == "/428":
      bot.send_message(message.from_user.id, "znacheniya3")
  elif message.text == "/427":
      bot.send_message(message.from_user.id, "znacheniya4")
  elif message.text == "/425":
      bot.send_message(message.from_user.id, znacheniya5)
  elif message.text == "/admin":
      bot.send_message(message.from_user.id, "+79197726735")
