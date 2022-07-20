import shutil
import os
from os import listdir
from os.path import isfile, join
import random

def read_dic(mypath:str)-> list:
    onlyfiles = [mypath + '/'+f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def rename(old_name, new_name):
    # Renaming the file
    os.rename(old_name, new_name)

loc = '/Users/huangkexin/Desktop/data/DCL_B'
listf = read_dic(loc)
print(listf)

with open('DCLB.txt', 'w') as fp:
    i = 0
    for item in listf:
        # write each item on a new line
        rename(item,loc+'/'+str(i)+'.jpg')
        fp.write(str(i)+ " %s\n" % item)
        i+=1
    print('Done')
