#!/usr/bin/python2
#-*- coding: utf-8 -*-
#marshal py2

'''
PyMarshal - Compile Python Script
This project was created by Dfv47 with Black Coder Crush. 
Copyright 12 - 07 - 2k19 @m_d4fv
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '3':
        exit("[sorry] use python version 2")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy2 = """
\033[0;92m╔══════════════════════════════════════════════╗
\033[0;32m║ ███    ██  \033[0;31m█████  \033[0;93m██    ██  \033[0;32m█████  \033[0;31m███    ██\033[0;92m ║
\033[0;32m║ ████   ██ \033[0;31m██   ██  \033[0;93m██  ██  \033[0;32m██   ██ \033[0;31m████   ██\033[0;92m ║
\033[0;32m║ ██ ██  ██ \033[0;31m███████   \033[0;93m████   \033[0;32m███████ \033[0;31m██ ██  ██\033[0;92m ║
\033[0;32m║ ██  ██ ██ \033[0;31m██   ██    \033[0;93m██    \033c[0;32m██   \033[0;32m██ \033[0;31m██  ██ ██\033[0;92m ║
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
    print(bannerpy2)
    print (y+' ['+w+'#'+y+'] '+w+'Example '+y+':'+w+' /sdcard/dfv.py')
    file = raw_input(y+' ['+w+'?'+y+'] '+w+'Input your file location'+y+' :'+w+' ')
    dfv = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+file+'"\n')
        sys.exit()
    try:
        code = compile(strng, '<daffa>', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        sys.exit()
fileout = open(o + '_Nayan_enc.py', 'wb')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('#Compiled By Mr. Nayan\n')
fileout.write('#https://github.com/MR-NAYAN-404\n')
fileout.write('#https://www.facebook.com/MR.NAYAN.45\n')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads('+repr(data)+'))')
fileout.close()
time.sleep(3) 
print (y+'\n ['+w+'+'+y+'] '+w+'File succes to compile   '+y+': ' + w + dfv + '_Nayan_enc.py\n')
