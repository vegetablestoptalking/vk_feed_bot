import telebot as tb
import config_bot as config
import sql_bot as sq
import feed_stream
sql = sq.sql_bot()

bot = tb.TeleBot(config.token_tg)
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я приватный бот @vegetablestoptalking. '
                                      'Если ты его друг, и он разрешил пользоваться мной, то введи /auth [логин] [код приглашения]')

@bot.message_handler(commands = ['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id, 'Чтобы начать работу с ботом, нужно войти в систему - /auth [логин] [код приглашения]\n'
                                      'Если Вы однажды вошли в ситсему, то повторно вызывать /auth не требуется.\n'
                                      'Для получения новостей используйте /feed')

@bot.message_handler(commands = ['auth', 'Auth'])
def auth(message):
    try:
        loc, login, code = str(message.text).split(' ')
        flag = sql.auth(login, code, message.chat.id)
    except ValueError:
        flag = False
    if flag:
        bot.send_message(message.chat.id, 'Вход выполнен!')
    else:
        bot.send_message(message.chat.id, 'Неверные данные!')

@bot.message_handler(commands=['feed', 'Feed'])
def feed(message):
    if not(sql.check_id(message.chat.id)):
        return
    s = ''
    feeds = feed_stream.FeedStream(sql.get_token_vk(message.chat.id))
    text = feeds.get_news()
    for item in text:
        s += item + '\n'
    bot.send_message(message.chat.id, s)





if __name__ == '__main__':
    bot.polling(none_stop=True)