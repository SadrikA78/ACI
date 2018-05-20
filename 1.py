# -*- coding: utf-8 -*-
# coding: utf8
from Tkinter import *
import Tkinter as tk
from PIL import ImageTk, Image
import os
from Tkinter import Button
import webbrowser
import twitter
import json
import time
import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from nltk.stem.snowball import SnowballStemmer
import string
from nltk.stem.porter import PorterStemmer
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, models, similarities 
import gensim
import os 
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.manifold import MDS
from sklearn.decomposition import NMF
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
from collections import Counter
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import wikipedia
import nltk
import time
import datetime
import json
import ast
import httplib
import urllib
import xlwt
import xlrd
import calendar
import time
import datetime
import httplib
import urllib
import json
import ast
import csv
import sys
import codecs
import sched, time
import threading
import xlwt
import xlrd
import time
font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True
style0 = xlwt.XFStyle()
style0.font = font0

#rb = xlrd.open_workbook('GAUN.xls',formatting_info=True)
#sheet = rb.sheet_by_index(0)
#---------------------------------------------------------------обучение определения тональности
name='Сюда писать ИМЯ'
last_name='ФАМИЛИЮ'
def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent.decode('utf-8'))})
pos = []
with open("pos_tweets.txt") as f:
    for i in f: 
        pos.append([format_sentence(i), 'pos'])
neg = []
with open("neg_tweets.txt") as f:
    for i in f: 
        neg.append([format_sentence(i), 'neg'])
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]
classifier = NaiveBayesClassifier.train(training)
classifier.show_most_informative_features()
def callback():
    #----------------------------------------------------------------------обращение к API Twitter

    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    tweet=twitter_api.search.tweets(q=(str(last_name)), count="100")
    p = json.dumps(tweet)
    res2 = json.loads(p)
    #print u'Получено сообщений: ',len(res2['statuses'])
    #----------------------------------------------------------------------формирование окна выдачи результатов
    stopwords = nltk.corpus.stopwords.words('english')
    en_stop = get_stop_words('en')
    stemmer = SnowballStemmer("english")
    #print stopwords[:10]
    total_word=[]
    lang=[]
    i=0
    retweet_count=[]
    followers_count=[]
    friends_count=[]
    tonal=[]

    #--------------------------------------------------------------------------оцека распространения


    cc=get_vk(name, last_name)
    p = ast.literal_eval(cc)
    if 'response' in p:
        file_inst = open('Rezult.html','w')
        file_inst.write('<html>')
        file_inst.write('<br>')
        #print (p['response']['items'][0]['first_name'].decode('utf-8'))
        a1='Фамилия: '+str(p['response']['items'][0]['first_name'])
        file_inst.write(a1)
        a2='Имя: '+str(p['response']['items'][0]['last_name'])
        file_inst.write('<br>')
        file_inst.write(a2)
        pp=ast.literal_eval((get_vk_2(p['response']['items'][0]['id'])))
        file_inst.write('<br>')
        if 'response' in pp:
            if len(pp['response'][0]['photo_200'])>0:
                file_inst.write('<img src='+str(pp['response'][0]['photo_200'])+'><br>')
                file_inst.write('<br>')
            if 'bdate' in pp['response'][0]:
                a3='Дата рождения: '+ str(pp['response'][0]['bdate'])
                file_inst.write(a3)
                
            if 'home_town' in pp['response'][0]:
                if len(pp['response'][0]['city']['title'])>0:
                    a4=', город рождения: ' + str(pp['response'][0]['home_town'])
                    file_inst.write(a4)
                    file_inst.write('<br>')
            if 'city' in pp ['response'][0]:
                if len(pp['response'][0]['city']['title'])>0:
                    a5='Город проживания: '+str(pp['response'][0]['city']['title'])
                    file_inst.write(a5)
                    file_inst.write('<br>')
            #if 'country' in pp['response'][0]:
                #ws.write(i,0, str(pp['response'][0]['country']['title'].decode('utf-8')))

            
            if 'career' in pp['response'][0]:
                if len(pp['response'][0]['career'])>0:
                    a6='Должность: '+ str (pp['response'][0]['career'][-1]['position'])
                    file_inst.write(a6)
                    file_inst.write('<br>')
            if 'domain' in pp['response'][0]:
                if len(pp['response'][0]['domain'])>0:
                    a7='Домен: '+str(pp['response'][0]['domain'])
                    file_inst.write(a7)
                    file_inst.write('<br>')
            #if 'site' in pp['response'][0]:           
                #ws.write(i,0, str(pp['response'][0]['site'].decode('utf-8')))
            #if 'home_phone' in pp['response'][0]:  
                #ws.write(i,0, str(pp['response'][0]['home_phone'].decode('utf-8')))
            if 'mobile_phone' in pp['response'][0]:
                if len(pp['response'][0]['mobile_phone'])>0:
                    a8='Телефон: '+str(pp['response'][0]['mobile_phone'])
                    file_inst.write(a8)
                    file_inst.write('<br>')
            #rb = xlrd.open_workbook('VK.xls',formatting_info=True)
            #sheet = rb.sheet_by_index(0)
            #for rownum in range(sheet.nrows):
                #row = sheet.row_values(rownum)
            

            #file_inst.write('http://vk.com/id'+row[3]+'<br>')
            
                #i=i+1
            file_inst.write('<br>')

            file_inst.write('************************  Упоминание  ****************************')
            file_inst.write('<br>')
            file_inst.write('<br>')
            while i<len(res2['statuses']):
                tweet=str(i+1)+') '+str(res2['statuses'][i]['created_at'])+' '+(res2['statuses'][i]['text'])+'\n'
                #t1.insert(END, (tweet))
                lang.append(res2['statuses'][i]['lang'])
                retweet_count.append(res2['statuses'][i]['retweet_count'])
                followers_count.append(res2['statuses'][i]['user']['followers_count'])
                friends_count.append(res2['statuses'][i]['user']['friends_count'])
                tokenizer = RegexpTokenizer(r'\w+')
                if 'en' in res2['statuses'][i]['lang']:
                   tonal.append(classifier.classify(format_sentence(res2['statuses'][i]['text'].encode('utf-8'))))
                total_word.extend(tokenizer.tokenize(res2['statuses'][i]['text']))        
                i=i+1
                file_inst.write(tweet.encode('utf-8'))
                file_inst.write('<br>')
                file_inst.write('<br>')
                file_inst.write('<br>')


            texts = []
            stopped_tokens = [i for i in total_word if not i in en_stop]
            #print len(stopped_tokens)
            p_stemmer = PorterStemmer()
            stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
            #print len(stemmed_tokens), stemmed_tokens
            texts.append(stemmed_tokens)
            dictionary = corpora.Dictionary(texts)
            corpus = [dictionary.doc2bow(text) for text in texts]
            ldamodel = gensim.models.LdaModel(corpus, num_topics=100, id2word = dictionary, passes=20)
            a=ldamodel.print_topics(num_topics=10, num_words=7)
            #print ldamodel.print_topics(num_topics=4, num_words=7)[0][1]
            #print a
            num_topics = 5
            topic_words = []
            for i in range(num_topics):
                tt = ldamodel.get_topic_terms(i,20)
                topic_words.append([dictionary[pair[0]] for pair in tt])
            #print topic_words[0]
            jj=0
            while jj<len(topic_words):
                topic11=((u"Тема #%d:" % (jj+1))+"\n"+"-".join(topic_words[jj])+"\n")
                #t8.insert(END, topic11)
                print(u"Тема #%d:" % (jj+1))
                print(" ".join(topic_words[jj]))
                jj=jj+1    
            #--------------------------------------------------------------------------определение основных тем
            vec = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_df=.5)
            tfv = vec.fit_transform(stopped_tokens)
            terms = vec.get_feature_names()
            #print type(terms)
            wc = WordCloud(height=1000, width=1000, max_words=1000).generate(" ".join(terms))
            nmf = NMF(n_components=11).fit(tfv)


            
            file_inst.write('************************  КОНТЕКСТ  ****************************')
            file_inst.write('<br>')
            file_inst.write('<br>')
            a9='Количество ретвитов: ' + str(sum(retweet_count))
            file_inst.write(a9)
            file_inst.write('<br>')
            a10='Возможный охват: ' + str(sum(followers_count)+sum(friends_count))
            file_inst.write(a10)
            file_inst.write('<br>')
            #file_inst.write(a12)
            #file_inst.write('<br>')
            file_inst.write('</html>')
            file_inst.close()
def get_vk(screen_name, screen_lastname):
    get_request =  '/method/users.search?q=' + screen_name
    get_request+= '%20'+screen_lastname
    get_request+= '&v=5.68'
    get_request+= '&access_token='
    local_connect = httplib.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    a=local_connect.getresponse().read()
    return a
def get_vk_2(id_user):
    get_request =  '/method/users.get?user_ids=' + str(id_user)
    get_request+= '&fields=photo_200%2C%20bdate%2C%20city%2C%20country%2C%20home_town%2C%20domain%2C%20has_mobile%2C%20contacts%2C%20site%2C%20last_seen%2C%20connections%2C%20career%2C%20military'
    get_request+= '&v=5.68'
    get_request+= '&access_token='
    local_connect = httplib.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    return local_connect.getresponse().read()
i=1
wb = xlwt.Workbook()
ws = wb.add_sheet(u'Ответ')
ws.write(0, 0,u'Фамилия',style0)
ws.write(0, 1,u'Имя',style0)
ws.write(0, 2,u'Дата рождения',style0)
ws.write(0, 3,u'Город проживания',style0)
ws.write(0, 4,u'Номер телефона',style0)
ws.write(0, 5,u'Электронный адрес',style0)
ws.write(0, 6,'Место работы',style0)
ws.write(0, 7,'Контекст',style0)

    
callback()
