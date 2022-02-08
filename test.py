#!/usr/bin/python

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print('Local datetime: ', now.toString())
print('Universal datetime: ', now.toUTC().toString(Qt.ISODate))

print(f'The offset from UTC is: {now.offsetFromUtc()} seconds')




import os
import datetime

today = datetime.datetime.now()
# dd/mm/YY
folder = today.strftime("%B_%d-%m-%Y__%H-%M-%S")

try:
    os.makedirs(folder)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise