import telebot
from telebot import types
import random

# SCRAPING
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5402213312:AAGLexLX0VMkdFFH4qbWSd3dzvJIGtzTesU")

proxies = [
'167.172.156.8:3128',
'100.24.5.242:3128',
'54.196.149.95:3128',
'51.81.80.109:3128',
'47.89.185.178:8888',
'3.82.203.47:3128',
'134.209.64.174:9999',
'216.37.138.177:3128',
'35.170.197.3:8888',
'167.114.185.69:3128',
'199.96.135.37:3128',
]
proxy=random.choice(proxies)

for proxy in proxies:
    print("\nChecking proxy:", proxy)
    try:
        page = requests.get('https://ipecho.net/plain', timeout=4, proxies={"http": proxy, "https": proxy})
        print("Status OK, Output:", page.text)
    except OSError as e:
        print(e)

# @bot.message_handler(commands=['start'])
# def button(message):
#     # bot.send_photo(message.chat.id, 'https://cdn1.picuki.com/hosted-by-instagram/q=0exhNuNYnjBcaS3SYdxKjf8P3||FyWgxSZ60STLepjSVmIR1vLHOapZA0mpCj4yRwKwVlASuRYz1o44gvU1xXCT15P0HcQbWJTDhd7K6bXOqjvDZl8JVpkb88LXAbY3Wu||sItVGCpNWwSDv5PHL||lo7gX5vPtcjEHpi2VNrQT9zJBpY6uSKVKz8B13bHR1Bv9vdBhYgJE8VQpMBQ7odLUvj8ESLn5M8on6PA5RbMCg8kW||+7piSS1X24ldihBGTOguYrVwr9Fui3rSzow+DyvVIcxLU1N0FeCsDcJ||68JvJSwcohp1KMZk6bTHEsAfU1KhjUok5e||ynSAPSam1x4Ck1||y9uuicfsqtJHnHaDOcN7RxznqZOnoOaIdZCI3CMX7SQiNDfq+LfBguL58P9dJkVGwrVDvVZGkjEtTQgpEgAuYBZYtFP+bwvf3')
#     # bot.send_video(message.chat.id, 'https://cdn2.picuki.com/hosted-by-instagram/q=0exhNuNYnjBcaS3SYdxKjf8C2OJ0Wg9SZ60STLepjSVmIR1vLHOapZA0mpCj4iRwKwVmASuSYz1o44svVl1YAz15O0TcSLSJRDdQ7a2RV+3N1DJh9JJkkb4wKXwWYXSs||8MlXAmYdS8ISqYVCayo+6Jt+pGJaWxXpFHOXLcgwAxLmJWNVpglycB5sKDVsk3h064iHm9850crJ1AFgYjXkA08V9j9AMJOqIcmRJ89g+smwffUrXy2EmBzKm1WOjmws6HDp80plRm5LWYCzEuhfY4NPE0mu1m4uRo3toIckr3wbd1X1ekxiZP9FSA4UW9UrwAzg5eymTfIZnTk20VFli2BjLC1fPcotYHxIuGcWJXqwyyGUb||dK7hNSSdeUKSQbFHfH||q+BJVqhox2DOxJ9Ha44yeFOeDzxAMkQjBOjmmqLbBSVfeo5o6F01aWlC7T8VBiyJvtLuIEng4JpJbfu1VEKiqWVJ0Xa2aAjhYdHN1||Z62VtrzfeM5zaSotG40+mEWHr5B9GiCArIwUY9NYC||Jar0sdRY||25tDivu50LKVEXHK0iZc6bsn6VilKJwaV53lGgEGmQSFt29lmwPdGi1567sV5orkGtjYUqEbMfpIEVbPjlxzqmf9noogHFkJnbqvemiqxMyNoiFZ86YdzCxNvE||XxWZHm6tDMjMjNZtqjQvRbVuR4y8WzK5SGYuhu04IRc+8Ny+sMDQCn8EHRN2m6SOzqNi5qjw4KgKCq0WtbtmtBPUGBh1Ja4Jlr5O2NSTusb7bd3bBGAJCNEUIfqaSeaRpUbUZnn+4KmJi4zuQgo3u71YF6L||oxYxv3dFuDz||Y2ZKUtL251jYwwYD7K8A1Yoih8oG2P457Dt7aJVTlK21uJMZpKcxFrG8vKzlg||cWTMtahg||wm||ILeCMoPzLuIJLRowSyHJ0i834Kiwvi2w4k2OTg==')
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     item = types.InlineKeyboardButton('Загрузить картинки', callback_data='refresh')
#     markup.add(item)
#
#     bot.send_message(message.chat.id, "Обновить картинки?:)", reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call:True)
# def parsing(call):
#     if call.message:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         item = types.InlineKeyboardButton('Котики', callback_data='cat')
#         item2 = types.InlineKeyboardButton('Уточки', callback_data='duck')
#         markup.add(item, item2)
#
#         if call.data == "refresh":
#             # search_text = [['cutest_duck', 'naknaq', 'grebcomics', 'duckorpenguin', 'crescentofsun', 'lilquackheads'], ['cats_of_instagram', 'ainegves', 'kotiki.kote', 'animals_prikoly', 'jimmyssunshinereport', 'softcatmemes', 'springmeal']]
#             for i in range(0, 2):
#                 file_name = ['duck_links.txt', 'cat_links.txt']
#                 tag = ["DUCKS", "CATS"]
#                 search_text = [['cutest_duck', 'naknaq', 'grebcomics'], ['cats_of_instagram', 'ainegves', 'kotiki.kote']]
#                 file_name = file_name[i]
#                 tag = tag[i]
#                 search_text = search_text[i]
#                 try:
#                     f = open(file_name, 'r+')
#                     f.truncate(0)
#                 except FileNotFoundError:
#                     f = open(file_name, 'a')
#                 bot.send_message(call.message.chat.id, f"Загружаем картинки {tag} ...")
#                 bot.send_message(call.message.chat.id, f"Это трохи долго, но это чисто загрузка, погуляй, я пришлю сообщение, когда все:)")
#                 links = []
#                 img_links = []
#                 video_links = []
#                 post_links = []
#                 for text in search_text:
#                     try:
#                         # print(proxy)
#                         # response = requests.get('https://www.picuki.com/profile/' + text, proxies={"http": proxy, "https": proxy})
#                         response = requests.get('https://www.picuki.com/profile/' + text)
#                         soup = BeautifulSoup(response.content, "html.parser")
#                         posts = soup.find_all("div", class_="photo")
#                         # print(soup.get_text())
#                         for post in posts:
#                             post_link = post.find_all('a')
#                             for link in post_link:
#                                 links.append(link.get('href'))
#                     except Exception as e:
#                         print(e)
#                 print("ссылки на посты, всего", len(links), links)
#                 for link in links:
#                     # response = requests.get(link, proxies={"http": proxy, "https": proxy})
#                     response = requests.get(link)
#                     soup = BeautifulSoup(response.content, "html.parser")
#                     try:
#                         picture = soup.find_all("div", class_="single-photo")
#                         for pic in picture:
#                             image = pic.find_all('img')
#                             for img_link in image:
#                                 img_links.append(img_link.get('src'))
#                         print('Фото:', len(img_links), img_links)
#                     except:
#                         picture = soup.find_all("div", class_="single-photo")
#                         for pic in picture:
#                             video = pic.find_all('video')
#                             for video_link in video:
#                                 video_links.append(video_link.get('src'))
#                         print('Видео:', len(video_links), video_links)
#                         pass
#                 # print(img_links)
#                 if len(video_links) == 0 and len(img_links) == 0:
#                     bot.send_message(call.message.chat.id, f"Блин, доступ получили к {tag}, но не вытянули картинки:(")
#                 else:
#
#                     with open(file_name, 'a') as f:
#                         for link in video_links:
#                             f.write(link + '#VIDEO')
#                             f.write('\n')
#                         for link in img_links:
#                             f.write(link)
#                             f.write('\n')
#                 bot.send_message(call.message.chat.id, f"Картиночки {tag} загрузил:)")
#             bot.send_message(call.message.chat.id, f"Все картиночки загрузил:)", reply_markup=markup)
#
#         elif call.data == "cat" or call.data == "duck":
#             if call.data == "cat":
#                 with open('cat_links.txt') as f:
#                     link = random.choice(f.readlines())
#                     if '#VIDEO' in link:
#                         link = link[0:-6]
#                         bot.send_video(call.message.chat.id, link, reply_markup=markup)
#                     else:
#                         bot.send_photo(call.message.chat.id, link, reply_markup=markup)
#             elif call.data == "duck":
#                 with open('duck_links.txt') as f:
#                     link = random.choice(f.readlines())
#                     if '#VIDEO' in link:
#                         link = link[0:-6]
#                         bot.send_video(call.message.chat.id, link, reply_markup=markup)
#                     else:
#                         bot.send_photo(call.message.chat.id, link, reply_markup=markup)
#
# bot.polling()