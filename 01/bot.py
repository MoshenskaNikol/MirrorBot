# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # �������� ������� �� ������ ������� ����, � ��������
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "������, ��� python!")
    	

if __name__ == '__main__':
     bot.polling(none_stop=True)