
# coding: utf-8

# In[18]:

import os
from ftplib import FTP
from ftplib import FTP_TLS
from subprocess import call
import shutil
import time


# In[19]:

ftp = FTP ('edc.dgfi.tum.de')
ftp.login()
ftp.cwd('/pub/slr/cpf_predicts/current/')


# In[20]:

print("program started")
time.sleep(1)


# In[21]:

with open('D:\eph/black_list.txt', 'r') as file:
    black_list = file.read().replace('\n','')


# In[22]:

file_names = ftp.nlst()

uniqs = []

for n in file_names:
    base = n.split('_')[0]
    if not base in uniqs and not base in black_list:
        uniqs.append(base)


all_last_files = []

print("# received all last file names")

time.sleep(0.5)


# In[23]:

for u in uniqs:
    masiv = []
    ftp.dir(u + '*', masiv.append)
    all_last_files.append(masiv[-1].split(' ')[-1])


# In[24]:

newpath = r'D:\eph\WOW1' 

if os.path.exists(newpath):
    shutil.rmtree(newpath)
else:
    os.makedirs(newpath)  


# In[25]:

savedir = 'D:\eph\WOW1'
os.chdir(savedir)


# In[26]:

for u in all_last_files:
    file = open(u, 'wb')
    ftp.retrbinary("RETR " + u, file.write)
    file.close()


# In[38]:

with open('D:\eph\ephem', 'w+') as outfile:
    for fname in all_last_files:
        with open(fname) as infile:
            outfile.write(infile.read())
            outfile.write("\n")
            


# In[14]:

savedir = 'D:\eph'
os.chdir(savedir)


# In[15]:

shutil.rmtree('D:\eph\WOW1')


# _____________________________________________________________________________________________________________________________

# In[62]:

#ftp = FTP_TLS('ftps://sentinelspodext.gmv.com')
#ftp = FTP_TLS('146.255.101.161')
#146.255.101.161
#ftp = FTP_TLS('sentinelspodext.gmv.com')
#cpodextftp.gmv.com
ftp = FTP_TLS('cpodextftp.gmv.com')
ftp.login(user='glsl', passwd = 'JrBdMe7s')
ftp.prot_p()
ftp.cwd('/slr/predicts/sentinel3a/')


# In[63]:

newpath = r'D:\eph\WOW2' 

if os.path.exists(newpath):
    shutil.rmtree(newpath)
else:
    os.makedirs(newpath) 


# In[64]:

savedir = 'D:\eph\WOW2'
os.chdir(savedir)


# In[65]:

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


# In[66]:

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


# In[67]:

filenames = [sentinel3a[0], sentinel3b[0]]
with open('D:\eph\ephem', 'a+') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
            outfile.write("\n")


# In[68]:

savedir = 'D:\eph'
os.chdir(savedir)
shutil.rmtree('D:\eph\WOW2')


# _____________________________________________________________________________________________________________________________
