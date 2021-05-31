# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:30:07 2021

@author: mikha
"""

import requests
import csv
import codecs
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

class yktForum:
    name = str
    link = str

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __repr__(self):
        return str(self.__dict__)

session = requests.session()
headers = {
    'authority': 'www.yeezysupply.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}
print('Start')
page=1

#f = open("scrapped_text.txt", "w")
#f = codecs.open("scrapped_text.txt", "w", "utf-8")

#for i in range(1,541):

for i in range(1,3):
    f = codecs.open("scrapped_text{id}.txt".format(id=page), "w", "utf-8")
    print("*****************************************************")
    link="https://forum.ykt.ru/viewforum.jsp?id=149&page="
    page+=1
    link2=link+str(i)
    print(link2)
    mikresponse1=session.get(link2, headers=headers)
    
    if mikresponse1.status_code == 200:
        print("Success link {}".format(link2))
        miksoup1 = BeautifulSoup(mikresponse1.text, 'html.parser')
        
        for element2 in miksoup1.find_all('div', {"class": "f-topic f-topic--brief"} ):
            try:
                row = element2.find('a', {"class": "emojify"})
                #sahaly_topic=str(row.contents[0]).encode('utf8')
                sahaly_topic=str(row.contents[0])
                print("Topic: {}".format(sahaly_topic))             
                f.write("++++++\n")
                f.write("{}\n".format(sahaly_topic))
                link_message = "https://forum.ykt.ru"+row.get('href')
                print(link_message)
                mikresponse2 = session.get(link_message, headers=headers)
                if mikresponse2.status_code == 200:
                    print("Successfully read topic {}".format(sahaly_topic))
                    miksoup2 = BeautifulSoup(mikresponse2.text, 'html.parser')

                    text_read=False
                    text=""
                    row_text=miksoup2.find('div', {"class": "f-view_topic-text emojify"} )
                    for row in row_text.find_all(text=True):
                        text=text + " " + str(row)
                    text_read=True
                    if text_read:
                            print("topic_text: {}".format(text))
                            f.write("------")
                            f.write("{}\n".format(text))
                    
                    for element3 in miksoup2.find_all('div', {"class": "f-comment_text"} ):                               
                        message_read=False
                        message=""
                        try:
                            element4=element3.find('p', {"class": "emojify"})                          
                            for row in element4.find_all(text=True):
                                message=message + " " + str(row)
                            message_read=True                        
                        except:
                            pass                        
                        if message_read:
                            print("Read message: {}".format(message))
                            f.write("******\n")
                            f.write("{}\n".format(message))               
                else:
                    print("Bad result: ", link2)
                mikresponse2.close()
            except:
                pass
    else:
        print("Unsuccess ",link2)
    mikresponse1.close()
f.close()    
print('Final')
