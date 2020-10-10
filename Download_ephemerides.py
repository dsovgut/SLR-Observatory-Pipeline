
# coding: utf-8

# In[18]:

import os
from ftplib import FTP
from ftplib import FTP_TLS
from subprocess import call
import shutil
import time


# In[19]:

ftp = FTP ('address')
ftp.login()
ftp.cwd('prediction_directory')


# In[20]:

print("program started")
time.sleep(1)


#make a blacklist.txt file and input the satellites you don't want to observe
with open('D:\eph/black_list.txt', 'r') as file: 
    black_list = file.read().replace('\n','')

file_names = ftp.nlst()

#getting satellite names from the server
uniqs = []
for n in file_names:
    base = n.split('_')[0]
    if not base in uniqs and not base in black_list:
        uniqs.append(base)


all_last_files = []

print("# received all last file names")

time.sleep(0.5)


for u in uniqs:
    masiv = []
    ftp.dir(u + '*', masiv.append)
    all_last_files.append(masiv[-1].split(' ')[-1])

#creating a temporary folder to store files
newpath = r'D:\eph\WOW1' 

if os.path.exists(newpath):
    shutil.rmtree(newpath)
else:
    os.makedirs(newpath)  

savedir = 'D:\eph\WOW1'
os.chdir(savedir)


for u in all_last_files:
    file = open(u, 'wb')
    ftp.retrbinary("RETR " + u, file.write)
    file.close()

with open('D:\eph\ephem', 'w+') as outfile:
    for fname in all_last_files:
        with open(fname) as infile:
            outfile.write(infile.read())
            outfile.write("\n")
            
savedir = 'D:\eph'
os.chdir(savedir)

#deleating temporary folder
shutil.rmtree('D:\eph\WOW1')

#retreiving sentinel from a separate connection
ftp = FTP_TLS('website.gov') #input your own website
ftp.login(user='user', passwd = 'passwd') #input your own credentials
ftp.prot_p()
ftp.cwd('/slr/predicts/sentinel3a/') #address of the sentinel data on the IRLS server

#creating a temp folder for sentinel data
newpath = r'D:\eph\WOW2' 

if os.path.exists(newpath):
    shutil.rmtree(newpath)
else:
    os.makedirs(newpath) 

savedir = 'D:\eph\WOW2'
os.chdir(savedir)

file_names = ftp.nlst()

uniqs = []

for n in file_names:
    base = n.split('_')[0]
    if not base in uniqs:
        uniqs.append(base)


sentinel3a = []

for u in uniqs:
    masiv = []
    ftp.dir(u + '*', masiv.append)
    sentinel3a.append(masiv[-1].split(' ')[-1])

file = open(sentinel3a[0], 'wb')
ftp.retrbinary("RETR " + sentinel3a[0], file.write)
file.close()


ftp.cwd('/slr/predicts/sentinel3b/')

file_names = ftp.nlst()

uniqs = []

for n in file_names:
    base = n.split('_')[0]
    if not base in uniqs:
        uniqs.append(base)


sentinel3b = []

for u in uniqs:
    masiv = []
    ftp.dir(u + '*', masiv.append)
    sentinel3b.append(masiv[-1].split(' ')[-1])

file = open(sentinel3b[0], 'wb')
ftp.retrbinary("RETR " + sentinel3b[0], file.write)
file.close()

#adding sentinel data to the ephemerides file
filenames = [sentinel3a[0], sentinel3b[0]]
with open('D:\eph\ephem', 'a+') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
            outfile.write("\n")

savedir = 'D:\eph'
os.chdir(savedir)
shutil.rmtree('D:\eph\WOW2')


# _____________________________________________________________________________________________________________________________
