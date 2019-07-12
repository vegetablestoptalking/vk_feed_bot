# -*- coding: utf-8 -*-
import vk_api
f = open('get_news.mireahacker228', 'w', encoding='utf8')
from vk_api.streaming import VkStreaming
class FeedStream:
    def __init__(self, token_n):
        self.token = token_n
        self.session = vk_api.VkApi(token=self.token)
        self.vk = self.session.get_api()

    def get_news(self): #returns list of strings
        js = self.vk.newsfeed.get(count=5, filters='post')
        for item in js['items']:
            f.write(str(item['text']) + '\n')
            f.write('_____________________________________' + '\n')
        f.close()
        f1 = open('get_news.mireahacker228', 'r', encoding='utf-8')
        return f1.readlines()


    def get_feeds(self):
        self.session = vk_api.VkApi(token=self.token)
        streaming = VkStreaming(self.session)
        streaming.delete_all_rules()
        streaming.add_rule('вуз', 'мира')
        streaming.add_rule('Россия', 'Москва')
        streaming.add_rule('планета', 'мир')
        streaming.add_rule('Кот', 'Лето')
        return streaming.listen()



