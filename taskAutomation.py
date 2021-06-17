import webbrowser
import time
import os
import subprocess

def redirectToPage(time):

    curDir = os.getcwd()

    if time >= '08:20:00' and time <= '08:50:00':
        webbrowser.open_new_tab('https://www.google.com')
    elif time >= '08:55:00' and time <= '09:40:00':
        webbrowser.open_new_tab('https://www.google.com')
    elif time >= '09:45:00' and time <= '10:30:00':
        webbrowser.open_new_tab('https://www.google.com')
    elif time >= '10:35:00' and time <= '11:20:00':
        webbrowser.open_new_tab('https://www.google.com')
    elif time >= '11:25:00' and time <= '12:10:00':
        webbrowser.open_new_tab('https://www.google.com')
    elif time >= '12:15:00' and time <= '13:00:00':
        webbrowser.open_new_tab('https://www.google.com')
    elif time >= '14:05:00' and time <= '14:50:00':
        webbrowser.open('https://www.google.com')
    elif time < '08:25:00':
        print('There is no class right now!')
    else:
        webbrowser.open_new_tab('https://github.com/shreyas880/TaskAutomation/upload')
        webbrowser.open('')


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

redirectToPage(current_time)