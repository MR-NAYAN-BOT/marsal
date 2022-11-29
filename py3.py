#!/usr/bin/python3
#-*- coding: utf-8 -*-
#marshal py3

'''
PyMarshal - Compile Python Script
This project was created by Dfv47 with Black Coder Crush. 
Copyright 12 - 07 - 2k19 @m_d4fv
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3")
       
import os
import time
#os.system("xdg-open https://github.com/MR-NAYAN-404")
time.sleep(1)
os.system('clear')
print("\033[1;31m TOOL IS OPENING :")


animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["\033[0;93m[■□□□□□□□□□]","\033[0;94m[■■□□□□□□□□]", "\033[0;92m[■■■□□□□□□□]", "\033[0;91m[■■■■□□□□□□]", "\033[0;97m[■■■■■□□□□□]", "\033[0;32m[■■■■■■□□□□]", "\033[0;94m[■■■■■■■□□□]", "\033[0;93m[■■■■■■■■□□]", "\033[0;91m[■■■■■■■■■□]", "\033[0;92m[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


os.system("xdg-open https://github.com/MR-NAYAN-404")
time.sleep(1)

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy3 = """
\033[0;92m╔══════════════════════════════════════════════╗
\033[0;32m║ ███    ██  \033[0;31m█████  \033[0;93m██    ██  \033[0;32m█████  \033[0;31m███    ██\033[0;92m ║
\033[0;32m║ ████   ██ \033[0;31m██   ██  \033[0;93m██  ██  \033[0;32m██   ██ \033[0;31m████   ██\033[0;92m ║
\033[0;32m║ ██ ██  ██ \033[0;31m███████   \033[0;93m████   \033[0;32m███████ \033[0;31m██ ██  ██\033[0;92m ║
\033[0;32m║ ██  ██ ██ \033[0;31m██   ██    \033[0;93m██    \033[0;32m██   \033[0;32m██ \033[0;31m██  ██ ██\033[0;92m ║
\033[0;92m║ ██   ████ \033[0;31m██   ██    \033[0;93m██    \033[0;32m██   \033[0;32m██ \033[0;31m██   ████\033[0;92m ║
\033[0;92m╚══════════════════════════════════════════════╝
\033[0;92m╔═══════════════════════════════════════════╗\033[0;92m╔═══╗
\033[0;92m║➣\033[0;31m DEVOLPER   :   \033[0;34m       MR. NAYAN          ║\033[0;32m║ N ║
\033[0;92m║➣\033[0;33m FACEBOOK   :    \033[0;35m      Mohammad Nayan     ║\033[0;32m║ A\033[0;92m ║
\033[0;92m║═══════════════════════════════════════════║\033[0;32m║ Y\033[0;92m ║
\033[0;92m║➣\033[0;91m WHATSAPP   :    \033[0;92m      01615298449        ║\033[0;32m║ A\033[0;92m ║
\033[0;92m║➣\033[0;93m GITHUB     :     \033[0;94m     MR-NAYAN-404       ║\033[0;92m║ N\033[0;92m ║
\033[0;92m║➣\033[0;94m TOOLS      :      \033[0;93m    Py3 MARSHAL        ║\033[0;92m║ 😘║
\033[0;92m╚═══════════════════════════════════════════╝\033[0;92m╚═══╝
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

os.system('clear')
try:
    print(bannerpy3)
    print (y+' ['+w+'#'+y+'] '+w+'\033[0;93m➣Example '+y+':'+w+'\033[0;94m /sdcard/nayan.py\n')
    file = input(y+' ['+w+'?'+y+'] '+w+'\033[0;92mInput your file location'+y+' :'+w+' ')
    o = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+file+'"\n')
        os.system("xdg-open https://github.com/MR-NAYAN-404")
        sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
        print (R + '   ['+W+'!'+R+'] '+R+'[ '+W+'File already to compiled\n') 
        sys.exit()

fileout = open(o + '_Nayan_enc.py', 'w')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('#Compiled By Mr. Nayan\n')
fileout.write('#https://github.com/MR-NAYAN-404\n')
fileout.write('#https://www.facebook.com/MR.NAYAN.45\n')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3) 
print (y+'\n ['+w+'+'+y+'] '+w+'File succes to compile   '+y+': ' + w + o + '_Nayan_enc.py\n')
