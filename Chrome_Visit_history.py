#-*- coding:utf-8 -*-

import csv
import os
import sqlite3 as sql
import datetime
import socket
import getpass
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from urllib.parse import urlparse

def getFiletime(dtms):
	if(dtms == 0):
		return (0)
	else:
		seconds, micros = divmod(dtms, 1000000)
		days, seconds = divmod(seconds, 86400)
		return str(datetime.datetime(1601, 1, 1) + (datetime.timedelta(days, seconds, micros, hours =+ 9)))

# 왜 이름이 print_url 인가요? - print를 안하는데 말입니다.
# 파라매터명이 int인건 좀 이상합니다. value 나 좀 더 다른 이름이 좋지 않을까요?
# int 는 타입명과 헷갈려서
# rows는 파라매터로 받는게 더 좋아보입니다.
def print_url(int):
	for num,row in enumerate(rows):
		if(row[0] == int):
			temp = row[1]
			return temp

# 파라매터명이 int인건 좀 이상합니다. value 나 좀 더 다른 이름이 좋지 않을까요?
# int 는 타입명과 헷갈려서
# rows는 파라매터로 받는게 더 좋아보입니다.
def url_details(int):
	for num,row in enumerate(rows):
		if(row[0] == int):
			temp = row[2]
			return temp

# 파라매터명이 int인건 좀 이상합니다. value 나 좀 더 다른 이름이 좋지 않을까요?
# int 는 타입명과 헷갈려서
# rows는 파라매터로 받는게 더 좋아보입니다.
def url_count(int):
	for num,row in enumerate(rows):
		if(row[0] == int):
			temp = row[3]
			return temp

# 파라매터명이 int인건 좀 이상합니다. value 나 좀 더 다른 이름이 좋지 않을까요?
# int 는 타입명과 헷갈려서
# rows는 파라매터로 받는게 더 좋아보입니다.
def Last_Visit_time(int):
	for num,row in enumerate(rows):
		if(row[0] == int):
			temp = row[5]
			return str(getFiletime(temp))	

# 위의 함수들이 거의 비슷한 코드인데 리팩토링 가능할듯 한데요?
# 어떻게 하면 좋을까요?

def get_IP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = (s.getsockname()[0])
	s.close()
	return ip

def getMac() :

    cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get MACAddress /format:rawxml'
    xml_text = check_output(cmd)
    xml_root = fromstring(xml_text)

    nics = []
    keyslookup = {
        'MACAddress' : 'mac',
    }

    for nic in xml_root.findall("./RESULTS/CIM/INSTANCE") :
        n = {'mac':'',}

        for prop in nic :
            name = keyslookup[prop.attrib['NAME']]
            if prop.tag == 'PROPERTY':
                if len(prop):
                    for v in prop:
                        n[name] = v.text
        nics.append(n)

    return nics

# f1 = open('E:\chrome_url_info.txt', 'w+', encoding='utf8')
time = datetime.datetime.now()
curr_time = ("%s%s%s" % (time.year, time.month, time.day)) + '_' + time.strftime("%H%M%S")

computer_N = socket.gethostname()

f2 = open("C:\\Users\\Public\\Documents\\" + computer_N + '_'+ curr_time + '_ChromeHistory'+'.txt', 'w+', encoding='utf8')
# f2 = open('E:\chrome_history_info.txt', 'w+', encoding='utf8')

data_path = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'history')
#conn = sql.connect(r"C:\Users\gayou\AppData\Local\Google\Chrome\User Data\Default\History")
conn = sql.connect(history_db)

# 왜 cursor를 세 개나 쓰나요?
cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()

cur.execute("SELECT * FROM urls")
cur2.execute("SELECT url, visit_time FROM visits")
cur3.execute("SELECT url, id FROM urls")

rows = cur.fetchall()
rows2 = cur2.fetchall()
rows3 = cur3.fetchall()

nics = getMac()
for nic in nics :
	for k, v in nic.items() :
	    MAC = v
	    MAC2 = MAC.replace(':', '-')

script = "http://mail.naver.com/login"
parse = urlparse(script)[1]
print(parse)



#urls

# print('------------------------------------URL_INFOMATION-------------------------------------')
# for num,row in enumerate(rows):
# 	print (socket.gethostname())
# 	print ('URL list [' + str(num + 1) + ']' + '\n' + 'URL ' +  ': ' + str(row[1])
# 		+ '\n'+'Details ' +  ': ' + str(row[2]) + '\n'+'Visit_Count ' +  ': ' + str(row[3])
# 		+ '\n' + 'last_visit_time ' +  ': ' + getFiletime(row[5]).replace(" ", " : "))

# 	host_name = socket.gethostname()
# 	IP = str(get_IP())
# 	user_name =  getpass.getuser()
# 	url = (str(row[1]))
# 	datails = (str(row[2]))
# 	visit_count = (str(row[3]))
# 	last_visit_time = (getFiletime(row[5]).replace(" ", " : "))


	# f1.write("	")
	# f1.write(' : ')
	# f1.write(host_name)
	# f1.write(' : ')
	# f1.write(user_name)
	# f1.write(' : ')
	# f1.write(MAC2)
	# f1.write(' : ')
	# f1.write(IP)
	# f1.write(' : ')
	# f1.write(str((last_visit_time)))
	# f1.write(' : ')
	# f1.write(str((url)))
	# f1.write(' : ')
	# f1.write(str((datails)))
	# f1.write(' : ')
	# f1.write(str((visit_count)))
	# f1.write('\n')
			
print ('-------------------------------------------------------------------------------------\n')
print('\n')
print('\n')
print('\n')
print ('---------------------------------------------------------------------------------------')
print('-------------------------------------VISIT_HISTORY-------------------------------------')

for num,row in enumerate(rows2):
	print('Url_Id : ' + str(row[0]) + '\n' + 'URL: ' + print_url(row[0]) + '\n' + 'URI: ' + urlparse(print_url(row[0]))[1] + '\n' +'URL_Detail: ' + str(url_details(row[0])) 
		+ '\n'+ 'Visit_Time : ' + getFiletime(row[1]).replace(" ", " : ") + '\n' + 'URL_Count: ' + str(url_count(row[0])))

	print ('====================================================================================')

	host_name = socket.gethostname()
	IP = str(get_IP())
	user_name =  getpass.getuser()
	url = (print_url(row[0]))
	uri = urlparse(url)[1]
	datails = (str(url_details(row[0])))
	visit_time = (getFiletime(row[1]).replace(" ", ":::;"))
	last_visit_time = (Last_Visit_time(row[0]).replace(" ", ":::;"))
	count = str(url_count(row[0]))
	


	f2.write(host_name)
	f2.write(':::;')
	f2.write(user_name)
	f2.write(':::;')
	f2.write(IP)
	f2.write(':::;')
	f2.write(MAC2)
	f2.write(':::;')
	f2.write(str((visit_time)))
	f2.write(':::;')
	f2.write(last_visit_time)
	f2.write(':::;')
	f2.write(str((url)))
	f2.write(':::;')
	f2.write(str((uri)))
	f2.write(':::;')
	f2.write(str((datails)))
	f2.write(':::;')
	f2.write(str((count)))
	f2.write('\n')	


conn.close()
# f1.close()
f2.close()




