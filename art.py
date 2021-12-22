import pyfiglet
from termcolor import colored
valid_colors= ("red","green","yellow","blue","magenta","cyan","pink")

art = input("what would you like to print?  ")
color = input("what color would you like?   ")
if color not in valid_colors:
    color="yellow"
ascii_art = pyfiglet.figlet_format(art)
colored_ascii= colored(ascii_art, color=color)
print(colored_ascii)
 