import commands
import os
import time
import hashlib
import GenExt
import requests
import json
from PIL import Image
from Command import *
import platform
import json

Platform=platform.system()

def Hash_115(String):
    return os.popen('java UseDump '+str(String)).read()

def Gen_osspw(Account,PassWord,V_ssoext):
    Return=os.popen('java UseDump '+Account+' '+PassWord+' '+V_ssoext).read()
    print Return
    return Return

def Gen_sign(Account,PassWord,V__time):
    Return=os.popen('java UseDump '+Account+' '+PassWord+' '+V__time+' '+'X').read()
    print Return
    return Return

def GenDeviceID():
    return 'ffffffff-acf2-0e6d-0033-c5870033c587'

def GetMD5(Data):
	Hash=hashlib.md5()
	Hash.update(Data)
	return Hash.hexdigest()

def UrlBuild(Account,PassWord,DeviceID):
    Dict={}
    Dict['account']=Account
    Dict['_time']=str(int(time.time()*1000))
    Dict['device_id']=DeviceID
    Dict['sign']=Gen_sign(Account,PassWord,Dict['_time'])
    Dict['version']='2.0'
    Dict['ssoext']=GenExt.GenExt(13)
    Dict['ssopw']=Gen_osspw(Account,PassWord,Dict['ssoext'])
    Dict['device']='HUAWEI C8816'
    Dict['os_ver']='4.3'
    Dict['n_type']='wifi'
    Dict['m_type']='HUAWEI C8816'
    Dict['ssoid']=''
    Dict['ssoinfo']=''
    ToReturn=''
    for Item in Dict:
        ToReturn+=Item
        ToReturn+='='
        ToReturn+=Dict[Item]
        ToReturn+='&'
    ToReturn=ToReturn[:-1]
    return ToReturn

Header={
        ''
        'User-Agent': 'Mozilla/5.0 (HUAWEIC8816; 4.3; zh;) 115disk/5.0.0',
        'Cookie': '',
        'Content-Type': 'application/x-www-form-urlencoded',
        #'Content-Length': 289,
        'Accept': '*/*',
        'Accept-Encoding': 'gzip',
        'Host': 'proapi.115.com',
        'Connection': 'Keep-Alive'
}

def Scan(V):
    if type(V)==str:
        QRCode=requests.get(V).content
        with open('Tarsh/QRCode','wb') as File:
            File.write(QRCode)
        #File=open('Tarsh/QRCode',)
    else:
        V.save('Tarsh/QRCode')
    Final=os.popen(ZBar(Platform)+' '+'Tarsh/QRCode').read().split('scan/')[1][:-1]
    return Final

def ScanProcess(UID,V_ssoid,Cookies,V_user_id):
    Cookie=''
    for Item in Cookies:
        Cookie+=Item
        Cookie+='='
        Cookie+=Cookies[Item]
        Cookie+=';'
    Url='https://proapi.115.com/android/1.0/scan/prompt?ssoinfo='+V_user_id+':F1&user_id='+V_user_id+'&ssoid='+V_ssoid+'&info='+UID+'&app_ver=5.6.3'
    Header={
            'Cookie':Cookie,
            'User-Agent': 'Mozilla/5.0 (HUAWEIC8816; 4.3; zh;) 115disk/5.6.3',
            'Accept-Encoding': 'gzip',
            'Host': 'proapi.115.com',
            'Connection': 'Keep-Alive'
    }
    requests.get(Url,headers=Header,verify=False)
    time.sleep(1)
    Header['Content-Type']='application/x-www-form-urlencoded'
    Data='client=0&uid='+UID+'&key='+UID+'&user_id='+V_user_id+'&app_ver=5.6.3'
    requests.post('http://proapi.115.com/android/1.0/scan/slogin',headers=Header,data=Data)
    return True

#def LoginProcess()

if os.path.isfile('Data/Initialized'):
    if not os.path.isfile('Data/Credential.json'):
        from Config.Account import *
        Data=UrlBuild(Account['Account'],Account['PassWord'],GenDeviceID())
        Header['Content-Length']=str(len(Data))
        Request=requests.post('https://proapi.115.com/android/1.0/login',headers=Header,data=Data,verify=False)
        Credential=Request.content
        with open('Data/Credential.json','wb') as File:
            File.write(Credential)
    else:
        pass

Scand=raw_input()
UID=Scan(Scand)
File=open('Data/Credential.json')
Credential=File.read()
JSON=json.loads(Credential)
Cookied=JSON['cookie_set']
ssoidd=JSON['ssoid']
useridd=JSON['user_id']
ScanProcess(UID,ssoidd,Cookied,useridd)
