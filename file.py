import os
import datetime
from os import path

"""
Make a program that creates a file that gives you the current
- time
- date
"""

def start():

    update_file = open('update.txt','w')
    current_time = datetime.datetime.now()

    hour = abs(12 - current_time.hour)
    minute = current_time.minute
    date = str(current_time)

    update_file.write(f'Today\'s date is {date[:10]}\n')
    update_file.write(f'The current time is {hour}:{minute}')
    update_file.close()

start()

    




