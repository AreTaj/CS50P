# Figlet
# Problem Set 4

from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

# List of fonts
font_list = figlet.getFonts()

# First command line argument (#0) is filename, so exclude from count of arguments.
if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(font_list))
# First argument must be either "-f" or "--font" and must be in the list of figlet fonts.
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
    figlet.setFont(font=sys.argv[2])    # Count from 0 for indices.
else:
    sys.exit("Invalid usage.")

text = input("Text input: ")
print(figlet.renderText(text))


"""
text = "hello, world"
figlet.setFont(font="alphabet")
print(figlet.renderText(text))


figlet.getFonts()
set_font = input("Input a font: ")
figlet.setFont(font="alphabet")

n = input("Text input: ")
figlet = Figlet(n)
print("Output: ", figlet)
"""