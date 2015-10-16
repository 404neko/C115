#

cd .
find . -name "*.pyc"  | xargs rm -f
rm -rf Config/Account.py
rm -rf Data/Credential.json
rm -rf Data/Initialized
rm -rf Tarsh/*
git add *
sh