import fileinput
from os import sys


def changeAccent():
    print('Select your OLD ACCENT color')
    print("[0] White")
    print("[1] Red")
    print("[2] Orange")
    print("[3] Yellow")
    print("[4] Green")
    print("[5] Blue")
    print("[6] Purple\n")

    oldAccColor_choice = int(input(">: "))

    if oldAccColor_choice == 0:
        oldAccColor = "white"
    elif oldAccColor_choice == 1:
        oldAccColor = "red"
    elif oldAccColor_choice == 2:
        oldAccColor = "orange"
    elif oldAccColor_choice == 3:
        oldAccColor = "yellow"
    elif oldAccColor_choice == 4:
        oldAccColor = "green"
    elif oldAccColor_choice == 5:
        oldAccColor = "blue"
    elif oldAccColor_choice == 6:
        oldAccColor = "purple"


    print('\nSelect your NEW ACCENT color')
    print("[0] White")
    print("[1] Red")
    print("[2] Orange")
    print("[3] Yellow")
    print("[4] Green")
    print("[5] Blue")
    print("[6] Purple\n")

    newAccColor_choice = int(input(">: "))

    if newAccColor_choice == 0:
        newAccColor = "white"
    elif newAccColor_choice == 1:
        newAccColor = "red"
    elif newAccColor_choice == 2:
        newAccColor = "orange"
    elif newAccColor_choice == 3:
        newAccColor = "yellow"
    elif newAccColor_choice == 4:
        newAccColor = "green"
    elif newAccColor_choice == 5:
        newAccColor = "blue"
    elif newAccColor_choice == 6:
        newAccColor = "purple"


    with fileinput.FileInput("mmarkex.py", inplace=True) as file:
        for line in file:
            print(line.replace(oldAccColor, newAccColor), end='')



def changeText():
    print('\nSelect your OLD TEXT color')
    print("[0] White")
    print("[1] Red")
    print("[2] Orange")
    print("[3] Yellow")
    print("[4] Green")
    print("[5] Blue")
    print("[6] Purple\n")

    oldTxtColor_choice = int(input(">: "))

    if oldTxtColor_choice == 0:
        oldTxtColor = "white"
    elif oldTxtColor_choice == 1:
        oldTxtColor = "red"
    elif oldTxtColor_choice == 2:
        oldTxtColor = "orange"
    elif oldTxtColor_choice == 3:
        oldTxtColor = "yellow"
    elif oldTxtColor_choice == 4:
        oldTxtColor = "green"
    elif oldTxtColor_choice == 5:
        oldTxtColor = "blue"
    elif oldTxtColor_choice == 6:
        oldTxtColor = "purple"


    print('\nSelect your NEW TEXT color')
    print("[0] White")
    print("[1] Red")
    print("[2] Orange")
    print("[3] Yellow")
    print("[4] Green")
    print("[5] Blue")
    print("[6] Purple\n")

    newTxtColor_choice = int(input(">: "))

    if newTxtColor_choice == 0:
        newTxtColor = "white"
    elif newTxtColor_choice == 1:
        newTxtColor = "red"
    elif newTxtColor_choice == 2:
        newTxtColor = "orange"
    elif newTxtColor_choice == 3:
        newTxtColor = "yellow"
    elif newTxtColor_choice == 4:
        newTxtColor = "green"
    elif newTxtColor_choice == 5:
        newTxtColor = "blue"
    elif newTxtColor_choice == 6:
        newTxtColor = "purple"


    with fileinput.FileInput("mmarkex.py", inplace=True) as file:
        for line in file:
            print(line.replace(oldTxtColor, newTxtColor), end='')

print("\n" * 999)

changeAccent()
changeText()

print("\nThe colors were succesfully changed!\n")
