#!/usr/bin/python
# author : Htmldigger
# Date : 4thfeb2022
# ## #####################################################
# Import Module here.
import os
import datetime
from getpass import getuser

# Added color to python terminal
# print("\033[1;32m This text is Bright Green  \n")

# UserName from system.
uName = getuser().capitalize()

# Now Time gather
today = datetime.datetime.now()

# dd/mm/YY
folder = today.strftime("%B_%d-%m-%Y_{x}_%H-%M-%S").format(x=uName)

if uName == 'Rion':
    print("\033[1;32m************** Admin Panel **************")
    print(f"\nWelcome Back Admin.\nDate : {today}\n\n*****************************************\n")
    print('Creating your woring directory...')
    try:
        print(f'Hey {uName} welcome to HTMLDigger sucessfully created : {folder}')
        # os.makedirs(folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    print("\033[0m\n")
    print(folder)
else:
    print(f'Hey {uName} welcome to HTMLDigger world.')
