import telebot 
from telebot import types 
import firebase_admin 
from firebase_admin import credentials 
from firebase_admin import db


cred = credentials.Certificate('23.json') 
firebase_admin.initialize_app(cred,{ 
    'databaseURL':'https://project-525066091564704208-default-rtdb.firebaseio.com/'})
result =db.reference('')
b=result.get()

a=b['Болатов1']
c=b['Болатов2']
d=b['Болатов3']



app_name=' t.me/DoctorZapisbot' 
token='5411738159:AAE2IYlSLji5SaS8jQOu2N1kmO7rJjZLV2c' 
bot=telebot.TeleBot(token)
spec=''
day=''
time=''
@bot.message_handler(commands=['start'])


def start(message):



   k = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) 
   button_1 = types.KeyboardButton('Стоматолог') 
   button_2 = types.KeyboardButton('Терапевт')
   button_3 = types.KeyboardButton('Онколог')
   k.add(button_1, button_2, button_3) 
   bot.send_message(message.chat.id, 'Здравствуйте, вы открыли бот для записи к врачу. К какому специалисту  вы хотели бы записаться?',reply_markup=k)
@bot.message_handler (content_types=['text'])


def name(message):
  global spec
  spec=message.text
  if message.text=='Терапевт':
              
              k_1= types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) 
              for key in a:
                k_1.add(*[types.KeyboardButton(name) for name in key.split()])
              m = bot.reply_to(message,'Выберите удобный для вас день недели',reply_markup=k_1)
             
              bot.register_next_step_handler(m, name1)
              print(spec)
             
  elif message.text=='Стоматолог':
              k_2= types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) 
              for key in c:
                k_2.add(*[types.KeyboardButton(name) for name in key.split()])
              m = bot.reply_to(message,'Выберите удобный для вас день недели',reply_markup=k_2)
              bot.register_next_step_handler(m, name2)
    
  elif message.text=='Онколог':
              k_3= types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) 
              for key in d:
                k_3.add(*[types.KeyboardButton(name) for name in key.split()])
              m= bot.reply_to(message,'Выберите удобный для вас день недели',reply_markup=k_3)
              bot.register_next_step_handler(m, name3)

def name1(message):
              global day
              day=message.text
              for key in a:
                 if message.text==key:
                  k_4 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                  k_4.add(*[types.KeyboardButton(name) for name in a[key]])
                  l=bot.reply_to(message,'Выберите удобное для вас время',reply_markup=k_4)
                  
                  bot.register_next_step_handler(l, username)

def name2(message):
              global day  
              day=message.text
              for key in c:
               if message.text ==key:
                  k_5 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                  k_5.add(*[types.KeyboardButton(name) for name in c[key]])
                  l=bot.reply_to(message,'Выберите удобное для вас время',reply_markup=k_5)
                  bot.register_next_step_handler(l, username)


def name3(message):
              global day
              day=message.text
              for key in d:
               if message.text ==key:
                  k_6 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                  k_6.add(*[types.KeyboardButton(name) for name in d[key]])
                  l=bot.reply_to(message,'Выберите удобное для вас время',reply_markup=k_6)
                  bot.register_next_step_handler(l, username)


def username(message):
    global time
    time=message.text
    h=bot.send_message(message.chat.id,'Нам нужно ваше имя для записи. Напишите ваше полное имя',reply_markup='')
    bot.register_next_step_handler(h, getname)
def getname (message):
   username=message.text
   ref=db.reference('/users')
   ref.update({spec:{username:{day:time}}})
   print('Добавлено')
bot.polling()






                            
