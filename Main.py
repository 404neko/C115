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
import StringIO
import sys

tNone=StringIO.StringIO()

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
    return os.system(ZBar(Platform)+' '+'Tarsh/QRCode'+' >nul 2>nul'),Final

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
    sys.stderr=tNone
    tStdout=sys.stderr
    requests.get(Url,headers=Header,verify=False)
    sys.stderr=tStdout
    time.sleep(1)
    Header['Content-Type']='application/x-www-form-urlencoded'
    Data='client=0&uid='+UID+'&key='+UID+'&user_id='+V_user_id+'&app_ver=5.6.3'
    requests.post('http://proapi.115.com/android/1.0/scan/slogin',headers=Header,data=Data)
    return True

#def LoginProcess()

def YN(String):
    if String.lower()=='y':
        return 1
    else:
        if String.lower()=='n':
            return -1
        else:
            return 0

def CredentialCheck(Credential):
    if Credential.find('"error":""')==-1:
        return False
    try:
        JSON=json.loads(Credential)
    except:
        return False
    try:
        Cookied=JSON['cookie_set']
        ssoidd=JSON['ssoid']
        useridd=JSON['user_id']
    except:
        return False
    return True

if os.path.isfile('Data/Initialized'):
    if not os.path.isfile('Data/Credential.json'):
        try:
            from Config.Account import *
        except:
            os.system('python Initialize.py')
            try:
                from Config.Account import *
            except:
                print 'Can\'t create Account.py. Exit.'
                exit(-1)
        Data=UrlBuild(Account['Account'],Account['PassWord'],GenDeviceID())
        Header['Content-Length']=str(len(Data))
        sys.stderr=tNone
        tStdout=sys.stderr
        Request=requests.post('https://proapi.115.com/android/1.0/login',headers=Header,data=Data,verify=False)
        sys.stderr=tStdout
        Credential=Request.content
        with open('Data/Credential.json','wb') as File:
            File.write(Credential)
    else:
        while True:
            QRCodeUrl=raw_input('Please enter QRCode\'s url:')
            #http://www.115.com/scan/?ct=scan&ac=qrcode&uid=218cf9b0eee6a2ece5b89fa72520f9e5d9c93481&_t=1445010370287
            if QRCodeUrl.find('scan')!=-1 and QRCodeUrl.find('uid=')!=-1 and QRCodeUrl.find('ac=')!=-1:
                break
            else:
                print 'Not a QRCode url!'
                pass
        ReturnByScan=Scan(QRCodeUrl)
        if ReturnByScan[0]!=0:
            print('Run zbar failed. Exit.')
            exit(-1)
        else:
            UID=ReturnByScan[1]
        File=open('Data/Credential.json')
        Credential=File.read()
        if CredentialCheck(Credential):
            JSON=json.loads(Credential)
            V_Cookie=JSON['cookie_set']
            V_ssoid=JSON['ssoid']
            V_userid=JSON['user_id']
            if ScanProcess(UID,V_ssoid,V_Cookie,V_userid):
                print 'Success!'
            else:
                print 'Fail.'
        else:
            print 'Credential file can\'t check fail. Exit.'
            exit(-1)
