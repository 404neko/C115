cd .
del *.pyc /s
del Config\Account.py
del Data\Credential.json
del Data\Initialized
del Tarsh\* /s
cmd /K "git add *"