import os
import platform
from setup import colors
from setup.colors import r,g,y,c , b

logo = f"""
███▄▄▄▄   ███    █▄    ▄▄▄▄███▄▄▄▄   
███▀▀▀██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄ 
███   ███ ███    ███ ███   ███   ███ 
███   ███ ███    ███ ███   ███   ███ 
███   ███ ███    ███ ███   ███   ███ 
███   ███ ███    ███ ███   ███   ███ 
███   ███ ███    ███ ███   ███   ███ 
 ▀█   █▀  ████████▀   ▀█   ███   █▀  
                                     
   ▄██████▄     ▄████████ ███▄▄▄▄    
  ███    ███   ███    ███ ███▀▀▀██▄  
  ███    █▀    ███    █▀  ███   ███  
 ▄███         ▄███▄▄▄     ███   ███  
▀▀███ ████▄  ▀▀███▀▀▀     ███   ███  
  ███    ███   ███    █▄  ███   ███  
  ███    ███   ███    ███ ███   ███  
  ████████▀    ██████████  ▀█   █▀   
                    {c + "Author: "+y +"Mr Juice | follow me"}             
"""

c = colors
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")

def banner():
    print(c.ran + logo)
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on instagram.com/mr_juice7 ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Chat me on Telegram @Developer Juice ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/mrjuice01/ ", "- " * 3+c.ran + "|")



def banner2():
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram.com/mr_juice7 ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Chat me on Telegram @DeveloperJuice ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/mrjuice01/ ", "- " * 3+c.ran + "|")

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")

snake = f"""
           /^\/^\
         _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~"""

snake2 = f'''
               ______
          _.-""      ""-._
       .-'                `-.
     .'      __.----.__      `.
    /     .-"          "-.     \
   /    .'                `.    \
  J    /                    \    L
  F   J                      L   J
 J    F                      J    L
 |   J                        L   |
 |   |                        |   |
 |   J                        F   |
 J    L                      J    F
  L   J   .-""""-.           F   J
  J    \ /        \   __    /    F
   \    (|)(|)_   .-'".'  .'    /
    \    \   /_>-'  .<_.-'     /
     `.   `-'     .'         .'
       `--.|___.-'`._    _.-'
           ^         """"

------------------------------------------------

'''
