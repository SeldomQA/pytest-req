"""
pip install pyfiglet
"""
from pyfiglet import Figlet

text = "pytest - req"

f = Figlet(font='slant')

# 生成并打印字符画
ascii_art = f.renderText(text)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(ascii_art)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
