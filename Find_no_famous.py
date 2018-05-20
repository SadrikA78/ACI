# -*- coding: utf-8 -*-
from Tkinter import *
import time
import datetime
import json
import ast
import httplib
import urllib
import xlwt
import xlrd

def get_vk(screen_name, screen_lastname, birth_day, birth_month, birth_year):
    get_request =  '/method/users.search?q=' + screen_name
    get_request+= '%20'+screen_lastname
    get_request+= '&birth_day=' + str(birth_day)
    get_request+= '&birth_month=' + str(birth_month)
    get_request+= '&birth_year=' + str(birth_year)
    get_request+= '&v=5.68'
    get_request+= '&access_token='
    local_connect = httplib.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    a=local_connect.getresponse().read()
    return a
def execute():
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True
    style0 = xlwt.XFStyle()
    style0.font = font0
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0,u'ФАМИЛИЯ',style0)
    ws.write(0, 1,u'ИМЯ',style0)
    ws.write(0, 3,u'ССЫЛКА',style0)
    ws.write(0, 2,u'КОЛИЧЕСТВО СОВПАДЕНИЙ',style0)
    n=0
    
    with open('List1.json') as data_file:    
        data = json.load(data_file)
        #print len(data['List1'])
        print u'Проверка записей'
        while n<len(data['List1']):
            screen_name1=data['List1'][n]['name'].encode('utf-8')
            screen_lastname1=data['List1'][n]['lastname'].encode('utf-8')
            birth_day1=str(data['List1'][n]['day']).encode('utf-8')
            birth_month1=str(data['List1'][n]['month']).encode('utf-8')
            birth_year1=str(data['List1'][n]['year']).encode('utf-8')
            cc=get_vk(screen_name1, screen_lastname1, birth_day1, birth_month1, birth_year1)
            p = ast.literal_eval(cc)
            #print p
            j=len(p['response']['items'])
            jj=0
            if 'response' in p:
                
                if j!=0 and len(p['response']['items'])>0:
                    print n+1
                    print n+1,u"КОЛИЧЕСТВО РЕЗУЛЬТАТОВ: ", j
                    list_link=[]
                    for jj in range(0,j):
                        
                        link='https://vk.com/id'+str(p['response']['items'][jj]['id'])

                        list_link.append(link)
                    #for links in list_link:    
                        #linkss = 'HYPERLINK("'+links+'")'
                        #ws.write(n+1, 3,xlwt.Formula(linkss))

                    ws.write(n+1, 0, screen_name1.decode('utf-8'))
                    ws.write(n+1, 1, screen_lastname1.decode('utf-8'))                
                    ws.write(n+1, 2, str(j))
                    #ws.write(n+1, 3,'\n'.join(list_link))
                    if len(list_link)>0:
                        ll=3
                        for linksss in list_link:
                            llinkss = 'HYPERLINK("'+linksss+'")'
                            ws.write(n+1, ll,xlwt.Formula(llinkss))
                            ll=ll+1
                            
                    """
                    for links in list_link:
                        print links
                        link = 'HYPERLINK("http://stackoverflow.com/"; "SO")' 
                        sheet.write(0, 0, FORMULA(link)) 
                        T = u'ссылка'
                        formula = '"{} " & HYPERLINK("{}")'.format(T, links)
                        ws.write(n+1, 3,xlwt.Formula(formula))
                    """
                    
    
                else:
                    #print n, u"КОЛИЧЕСТВО РЕЗУЛЬТАТОВ: ", j
                    print n+1
                    ws.write(n+1, 1, str(j))
                    
            #else:
                #print n, "not rezult"
            time.sleep(3)
            n = n + 1
    #print u'КОНЕЦ ПОИСКА'
    wb.save('REZULT.xls')
    
 



def show_entry_login():
    a=1925900596
    value = datetime.datetime.fromtimestamp(a)
    aa=value.strftime('%d.%m.%Y')
    e4.insert(END, (u'До '+aa))
    """
    if e1.get()=='' and e2.get()=='':
        e4.insert(END, u'Верный пароль')
        with open('List1.json') as data_file:    
                data = json.load(data_file)
                rows=len(data['List1'])*3
                roiws=u'Время '+str(rows)+u' сек.'
                e5.insert(END,roiws)
    else:
        e4.insert(END, u'Не верный пароль')
    """
    
def show_entry_fields():
            
    execute()


master = Tk()
master.title('ПОИСК (Alfa)')
#Label(master, text=u"Логин").grid(row=0, column=0)
#Label(master, text=u"Пароль").grid(row=0, column=2)
#Label(master, text=u"Проверка").grid(row=1, column=1)
#Label(master, text=u"Выберете социальную сеть").grid(row=6, column=0)
#Label(master, text=u"Ключ доступа").grid(row=6, column=2)
#Label(master, text=u"Контроль прогресса").grid(row=7, column=1)
e1 = Entry(master)
e2 = Entry(master)
e3=Entry(master)
e4=Text(master, height=1, width=25)
#e5=Text(master, height=1, width=10)
#e1.grid(row=0, column=1, sticky=N, padx=5, pady=10)
#e2.grid(row=0, column=3, sticky=N, padx=5, pady=10)
#e3.grid(row=6,column=3)
e4.grid(row=1,column=2, columnspan=2, sticky=W+E+S, pady=5)
#e5.grid(row=7,column=2, columnspan=2, sticky=W+E+S, pady=5)
#var = StringVar(master)
#var.set("---\\---")
#option = OptionMenu(master, var, u"Вконтакте")
#option.grid(row=6, column=1, sticky=N+W+E+S, pady=5)
Button(master, text=u'Проверьте срок действия программы', command=show_entry_login).grid(row=1, column=0, sticky=N+W+E+S, pady=4)#""", command=show_entry_login"""
Button(master, text=u'Старт', command=show_entry_fields).grid(row=8, column=5, sticky=N+W+E+S, pady=4)
mainloop( )
