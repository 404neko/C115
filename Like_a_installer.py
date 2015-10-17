#coding:utf-8

import sys
import os
import Command
import platform

def Wa(String):
    print '!!!\nWarning: '+String

def Fa(String):
    print '!!!\nFail: '+String
    exit(-1)

def OK():
    print 'OK'

def P_ckf(String):
    print 'Checking for '+String+' ...',

P_ckf('python\'s version')
if sys.version[0]!='2':
    Wa(': running on python 3.x, there may some bugs.')
else:
    OK()

P_ckf('PIL')
try:
    import PIL
    OK()
except:
    Fa('PIL not found.')

P_ckf('Java(TM) $E Runtime Environment')
if os.system('java -version')==0:
    OK()
else:
    Fa('Java(TM) $E Runtime Environment not found.')

P_ckf('Java(TM) $E Development Kit')
if os.system('javac -version')==0:
    OK()
else:
    Wa('Java(TM) $E Development Kit not installed.')

P_ckf('ZBar')
if os.system(Command.ZBar(platform.system()))==0:
    OK()
else:
    Fa('ZBar not installed.')
