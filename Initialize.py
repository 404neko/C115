import os
import getpass
import platform

def CreatFolder(Path):
	if Path.find('/')==-1:
		if not os.path.exists(Path):
			os.mkdir(Path)
	else:
		Path=Path.split('/')
		Path0=''
		for PathItem in Path:
			Path0=Path0+PathItem+'/'
			if not os.path.exists(Path0):
				os.mkdir(Path0)

def SetAccount():
    Answer=''
    if(os.path.isfile('Config/Account.py')):
        while Answer.lower()!='y' and Answer.lower()!='n':
            Answer=''
            Answer=raw_input('Account info setted, reset it?[Y/N]')
        if Answer.lower()=='n':
            return True
        else:
            Set()
            return True
    else:
        Set()
        return True

def Set():
    AccountSetted=False
    while True:
        Account=raw_input('Please input account:')
        while True:
            Answer=''
            Answer=raw_input('Your account is: '+Account+'.[Y/N]')
            if Answer.lower()=='n':
                break
            else:
                if Answer.lower()=='y':
                    AccountSetted=True
                    break
        if AccountSetted:
            break
        else:
            pass
    PassWord=getpass.getpass('Enter password: ')
    File=open('Config/Account.py','w')
    File.write('Account={\'Account\':\''+Account+'\',\'PassWord\':\''+PassWord+'\'}')
    File.close()

if __name__=='__main__':
	CreatFolder('Config')
	CreatFolder('Data')
	CreatFolder('Tarsh')
	SetAccount()
	File=open('Data/Initialized','w')
	File.write('#Umaru~')
	File.close()
	File=open('Config/__init__.py','w')
	File.write('#Umaru~')
