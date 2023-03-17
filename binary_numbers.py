import random
import time
import os
"""
This is created just for time pass and provided open source by solohackerzorganization. 
Give credits if you use it and Have Fun.
May God Bless You All 
"""
ch = input('Press Enter To Start :')
timein = int(input('For How much time you want to print number (seconds) :'))
duration = timein
print('Remove Last digit of screen width \nFor Example is your width is 1280 Type: 128')
screen_width = int(input('Enter Screen Width : '))
print('Remove Last digit of screen Height \nFor Example is your height is 1024 Type: 102')
screen_height = int(input('Enter Screen Height : '))
os.system('clear')
colors = [
    '\033[31m',  # Red
    '\033[32m',  # Green
    '\033[33m',  # Yellow
    '\033[34m',  # Blue
    '\033[35m',  # Magenta
    '\033[36m',  # Cyan
    '\033[91m',  # Light Red
    '\033[92m',  # Light Green
    '\033[93m',  # Light Yellow
    '\033[94m',  # Light Blue
    '\033[95m',  # Light Magenta
    '\033[96m',  # Light Cyan
]
def solo():
    if '' in ch:
        start_time = time.time()
        while time.time() - start_time < duration:
            num_numbers = random.randint(1500, 4000)
            for i in range(num_numbers):
                color = random.choice(colors);x_pos = random.randint(0, screen_width - 8)
                y_pos = random.randint(0, screen_height - 1)
                binary_num = str(random.randint(0, 1))
                print('\033[{};{}H{}{}'.format(y_pos+1, x_pos+1, binary_num,color))
            time.sleep(0.13)
            for i in range(screen_height):
                print('\033[{};1H{}'.format(i+1, ' '*screen_width), end='')
            print('\033[1;1H')

solo()
