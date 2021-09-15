def InitColor(red = 0, green = 0, blue = 0, bold = False, dim = False, italic = False, underlined = False, swap_foreground_and_bg_colors = False, hidden = False, reset = False,reset_all = False):
  '''
  ```
  red, green, and blue: color to use throughout the code unless changed\n
  the rest of the parameters are self-explanantory for customization of the text\n
  reset: resets the attributes (Does not include the colors)\n
  reset_all: resets all of the attributes (Including colors)\n
  ```
  Syntax | Description
  --------- | ---------
  `\\033[0m` | Resets all color and formats
  `\\033[1m` | Creates bold text
  `\\033[2m` | Creates dim text
  `\\033[3m` | Creates italic text
  `\\033[4m` | Creates underlined text
  `\\033[7m` | Swaps foreground and background colors
  `\\033[8m` | Hides text
  `\\033[38;2;{RED};{GREEN};{BLUE}m` | Create custom colors using RGB color codes
  '''
  import os
  def clear():
    os.system('clear')
  if red > 255 or green > 255 or blue > 255 or red < 0 or green < 0 or blue < 0:
    print(f'Try again; Your inputs were:\nRED: {red}\nGREEN: {green}\nBLUE: {blue}\n One of them was too high or too low.')
  else:
    print(f'\033[38;2;{red};{green};{blue}m')
  clear()
  for i in range(2):
    if bold == True:
      print('\033[1m')
      clear()
      break
    elif dim == True:
      print('\033[2m')
      clear()
      break
    elif italic == True:
      print('\033[3m')
      clear()
      break
    elif underlined == True:
      print('\033[4m')
      clear()
      break
    elif swap_foreground_and_bg_colors == True:
      print('\033[7m')
      clear()
      break 
    elif hidden == True:
      print('\033[8m')
      clear()
      break
    elif reset == True:
      print('\033[0m')
      clear()
      print(f'\033[38;2;{red};{green};{blue}m')
      clear()
      break
    elif reset_all == True:
      print('\033[0m')
      clear()
      break