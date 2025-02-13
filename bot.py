import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

all_commands = {
    'hi' : 'Приветствие c именем',
    'start' : 'Приветсвие без имени',
    'hello' : 'Приветсвие без имени',
    'photo' : 'Скачивает твоё фото в папку IMG',
    'help' : 'Вывод всех команд'
}

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    bot.reply_to(message, "Скачал твою фотку")
    file_info = bot.get_file(message.photo[-1].file_id)
    download_file = bot.download_file(file_info.file_path)
    file_path = 'img/'+f'{message.photo[-1].file_id}.jpg'
    with open (file_path, 'wb') as file:
        file.write(download_file)
        
    
@bot.message_handler(commands=['hi'])
def send_welcom(message):
    user_name = message.text.split()
    len_user_name = len(user_name)
    if len_user_name>2:
        user_name = "foreign"
    else :
        user_name=user_name[1]
    bot.reply_to(message, f'Hi {user_name} !')
    
@bot.message_handler(commands=['help'])
def helper(message):
    bot.reply_to(message, "Вот мои команды: \n"+ "\n".join("/" + k for k in all_commands.keys()))
    
bot.polling()
