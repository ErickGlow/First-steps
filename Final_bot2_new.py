import telebot
import requests
from bs4 import BeautifulSoup
import time


token = "5048943814:AAEfabGJArLjZX1yRbMREvOZCjUyTXsPXo4"
CHANNEL_NAME = '@FinalProjectPy2022'
bot = telebot.TeleBot(token)


while True:
    html = requests.get(r'https://habr.com/ru/').text
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')
    for x in news:
        title = x.find('a').get_text()
        link = x.a.get('href')
        topics = (title+'\n\nhttps://habr.com' + link)
        print(topics)
        print('__________')
        bot.send_message(CHANNEL_NAME,topics)
        time.sleep(3)
    time.sleep((3600 * 24))

 


