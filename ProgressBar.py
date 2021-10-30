
from alive_progress import alive_bar, config_handler
from time import sleep
from random import randint
from InitColor import InitColor
import os
def clear():
  os.system('clear')

    

def terminated():
  InitColor(red = 255, green = 0, blue = 0, bold = True)
  print ('PROGRAM CRASHED\nPLEASE RESTART PROGRAM\nSESSION TERMINATED')
  exit()
  
def chance():
  InitColor(red = 255, green = 0, blue = 0)
  r = randint(1, 1000)
  if r == 392:
    terminated()
    exit()
  else:
    print('We ran into an internal error... Please Wait')
    sleep(randint(1, 3))
    print('Error Fixed.')
    sleep(1.5)
    clear()


def bar(amount = 1000, starting_string = 'Initializing...', bar = 'bubbles', spinner = 'dots'):
  InitColor(red = 0, green = 255, blue = 0)
  '''
  ```
  amount: the amount needed to end the progress bar\n
  startin_string: the string that is going to be printed out on 0\n
  bar: the type of bar that will used in the progress bar\n
  spinner: the tpye of spinner that will be used in the progress bar
  ```
  '''
  config_handler.set_global(bar = bar, spinner = spinner)
  count = 0
  with alive_bar(amount) as Bar:
    for i in range(amount):
      if count == 0:
        print(starting_string)
        sleep(1)
        clear()
        count += 1
        InitColor(red = 0, green = 255, blue = 0)
      elif i % randint(100, 700) == count - 1 and count != 0:
        chance()
        InitColor(red = 0, green = 255, blue = 0, reset = True)
        InitColor(red = 0, green = 255, blue = 0)
      sleep(0.01)
      Bar()
    print('\033[38;2;255;255;0mStarting up PyLator')
  sleep(1.5)