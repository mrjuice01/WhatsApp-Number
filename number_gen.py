# Use With Python 3
import os
try:
    import colorama
    from colorama import Style, Fore
except ModuleNotFoundError:
    os.system("pip install colorama")

try:
    import phonenumbers
except ModuleNotFoundError:
    os.system("pip install phonenumbers")
try:
    import fontstyle
except ModuleNotFoundError:
    os.system("pip install fontstyle")

import sys, random

from setup.banner import  banner2 , banner , clear
from setup.colors import r, g ,y  ,lg ,w
clear()

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)

k = all_col[2]

banner()
def exit():
    sys.exit()


l = [Style.BRIGHT + Fore.RED, Style.BRIGHT + Fore.LIGHTBLUE_EX, Style.BRIGHT + Fore.LIGHTCYAN_EX,
     Style.BRIGHT + Fore.LIGHTMAGENTA_EX, Style.BRIGHT + Fore.LIGHTYELLOW_EX, Fore.CYAN]

c = random.choice(l)
def randomcolors(n):

    c = random.choice(l)
    print(f"{c} {fontstyle.apply(n, 'bold')}")

def program():
    try:
        print('-' * 33)
        code = input(f'{c}Enter the Country Code [like +263 For Zimbabwe] : ')
        d = random.choice(l)
        print(d, '-' * 33)
        area_code = input(f'{d}Enter the Network code [ Like 263] : ')
        e = random.choice(l)
        print('-' * 33)
        n = int(input(f"{e}Enter Amount of numbers: "))
        print(e, '-' * 33)
        f = random.choice(l)
        lent = int(input(f'{f}Length Remaining Digits [ 10 FOR Zimbabwe🇿🇼 ] : '))
        print(f, '-' * 33)
        mow = str('9' * lent)
        print(c, '-' * 33)

        def number_generator():
            first = str(random.randint(0, int(mow))).zfill(lent)
            return (first)

        j = random.choice(l)

        save = open('numbers.txt', 'a+')
        for i in range(0, n):
            rez = code + area_code + number_generator()
            save.write(rez + '\n')
        print(f'{j}Phone Numbers Saved In numbers.txt')

    except ValueError:
        print(f"{k}\nYou have missed something")


    except KeyboardInterrupt:
        randomcolors("\nHave a good Day brother Thanks for Using My Tool:-)")

def view():
    file = open("numbers.txt" , "r")
    print(lg , "\n\t\tThis is what i've found!\n")
    read = file.read()
    method = read
    print(f"{ran} {method}")


def verification():
    file = r"numbers.txt"

    nums = [x.strip('\n') for x in open(file , "r").readlines()]

    for n , num in enumerate(nums):
        print(f"{g}Tyring to verify the number:{str(n)}{w} {num} ({r}{str(n)}/{str(len(nums))}")
        num = num.replace(" " , "")

        mob = phonenumbers.parse(num)

        print(f"{w}{num} Valid: {y}{phonenumbers.is_valid_number(mob)}")
        if phonenumbers.is_valid_number(mob) == True:
            with open("Valid_numbers" , "a+") as fi:
                fi.write(num)
        else:
            pass


cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTGREEN_EX + "\n\n\t\t[1] Generate Numbers\t\t\n\t\t[2] View Generated Numbers\n\t\t[3] Exit\n\t\t[4] Verify generated numbers\n")

    choice = input(ran + "Enter:~ ")
    if choice == "1":
        program()

    elif choice == "2":
        view()

    elif choice == "3":
        banner2()
        exit()

    elif choice == "4":
        verification()

    else:
        print(r + "\nInvalid option")
        exit()
    cont = input(y + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        clear()
        banner()














