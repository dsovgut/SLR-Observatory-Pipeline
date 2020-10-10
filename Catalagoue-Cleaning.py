
# coding: utf-8

# In[1]:

import ctypes
import itertools
import os
import string
import platform
import shutil
import time 
import sys

#function checking if a disk is connected  
def get_available_drives():
    if 'Windows' not in platform.system():
        return []
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(itertools.compress(string.ascii_uppercase,
               map(lambda x:ord(x) - ord('0'), bin(drive_bitmask)[:1:-1])))

#checking if disk z is connected
if 'Z' not in get_available_drives():
    print ("Connect Disk Z for program to work.")
else:
  print ("Disk Z is connected. Program Started.")

dpath = r'D:\archiv2\temp'
os.makedirs(dpath)  

#Clearing a catalog files on disk Z
path1 = r'Z:\spl\result\catalog.loc'
open(path1, 'w').close()

#deleating everything in the folder calibrate
folder = r'Z:\calibrate'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

#deleating everything in the folder calibrate1
folder = r'Z:\calibrate1'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

folder = r'Z:\locat'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

path2 = r'Z:\calibrate\catalog.kal'
open(path2, 'w').close()

start= r"D:\LASER-2\DATA\KAT_OBS.DIC"
end = r'D:\archiv2\temp'
shutil.copy(start,end)

start= r"D:\LASER-2\DATA\KAT_KAL.DIC"
end = r'D:\archiv2\temp'
shutil.copy(start,end)

start= r"D:\LASER-2\DATA\KAT_KBO.DIC"
end = r'D:\archiv2\temp'
shutil.copy(start,end)


# In[32]:

#copying the extensions files
source_directory_path = r"D:\LASER-2\DATA"
destination_directory_path = r'D:\archiv2\temp'

for source_filename in os.listdir(source_directory_path):
    if source_filename.endswith(".ega"):
        source_file_path = os.path.join(source_directory_path, source_filename)
        shutil.copy(source_file_path, destination_directory_path)
        
for source_filename in os.listdir(source_directory_path):
    if source_filename.endswith(".oga"):
        source_file_path = os.path.join(source_directory_path, source_filename)
        shutil.copy(source_file_path, destination_directory_path)
        
for source_filename in os.listdir(source_directory_path):
    if source_filename.endswith(".KGA"):
        source_file_path = os.path.join(source_directory_path, source_filename)
        shutil.copy(source_file_path, destination_directory_path)
        
for source_filename in os.listdir(source_directory_path):
    if source_filename.endswith(".LGA"):
        source_file_path = os.path.join(source_directory_path, source_filename)
        shutil.copy(source_file_path, destination_directory_path)
        
for source_filename in os.listdir(source_directory_path):
    if source_filename.endswith(".PGA"):
        source_file_path = os.path.join(source_directory_path, source_filename)
        shutil.copy(source_file_path, destination_directory_path)

for source_filename in os.listdir(source_directory_path):
    if source_filename.endswith(".CGA"):
        source_file_path = os.path.join(source_directory_path, source_filename)
        shutil.copy(source_file_path, destination_directory_path)
for source_filename in os.listdir(source_directory_path):
    if source_filename.endswith(".prn"):
        source_file_path = os.path.join(source_directory_path, source_filename)
        shutil.copy(source_file_path, destination_directory_path)



#getting specific extensions which start with T and K and have a number in them
import glob
path3 = r"D:\LASER-2\DATA"
os.chdir(path3)
files = []
for file in glob.glob('T?*.K*[0-99]'):
    files.append(file)
source = r'D:\archiv2\temp'
for u in files:
    shutil.copy(u,source)

#giving the temp folder a name with a date
from datetime import datetime
directory = r'D:\archiv2'
os.chdir(directory)
name = r'temp'
os.rename(name, datetime.today().strftime('%Y_%m_%d'))

#archiving files
shutil.make_archive(datetime.today().strftime('%Y_%m_%d'), 'zip', datetime.today().strftime('%Y_%m_%d'))

#deleating the folder, leaving only archived folder
shutil.rmtree(datetime.today().strftime('%Y_%m_%d'))

directory = r"D:\LASER-2\DATA"
os.chdir(directory)
open('KAT_OBS.DIC', 'w').close()
open('KAT_KAL.DIC', 'w').close()
open('KAT_KBO.DIC', 'w').close()


import glob
for file in glob.glob('*ega'):
    os.remove(file)
for file in glob.glob('*oga'):
    os.remove(file)
for file in glob.glob('*KGA'):
    os.remove(file)
for file in glob.glob('*LGA'):
    os.remove(file)
for file in glob.glob('*PGA'):
    os.remove(file)
for file in glob.glob('*CGA'):
    os.remove(file)
for file in glob.glob('*prn'):
    os.remove(file)
for file in glob.glob('T?*.K*[0-99]'):
    os.remove(file)

path4 = r"D:\LASER-2\DATA"
os.chdir(path4)
for file in glob.glob('T?*.K*[0-99]'):
    os.remove(file)

print('program completed')

