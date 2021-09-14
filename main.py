# Import all the needed modules
from translate import Translator
from time import sleep
import os
# And functions
from InitColor import InitColor

# Our prompt program
def prompt(_):
  prompt = input(f'{_}\n>')
  sleep(0.7)
  os.system('clear')
  return prompt
#Our translator program
def translate(convert_to = None, convert_from = None, text = None):
  InitColor(119, 255, 0)
  if convert_to:
    pass 
  else:
    convert_to = prompt('Language to be converted to (Default is english (en))')
    if not(convert_to):
      convert_to = 'en'
  if convert_from:
    pass
  else:
    InitColor(255, 119, 0)
    convert_from = prompt('Language to be converted from (Default is french (fr))')
    if not(convert_from):
      convert_from = 'fr'
  if text:
    pass
  else:
    InitColor(0,255,255)
    text = prompt(f'Text to be converted from {convert_from} to {convert_to}')
        
  translation = Translator(to_lang=convert_to, from_lang = convert_from).translate(text).capitalize()
  InitColor(119, 255, 0)
  print(f'Translated text ({convert_to}):\n  {translation}')
  print('\033[38;2;255;119;0m')
  print(f'Original text ({convert_from}):\n  {text}')

# Running our code!
translate()