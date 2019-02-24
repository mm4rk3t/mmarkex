import os # Needed to terminal commands and to scan directories and files
from os import sys # Needed to exit some commands
import random # Needed to select random files
import webbrowser # Needed to open websites
import time # Needed to 'time.sleep(#)
import colors # Own file (colors.py)


def main():

    accent_color = colors.blue
    text_color = colors.white

    coloblue_input = accent_color + ">: " + text_color


    awesome_name = "\n"*999  + """

    ███▄ ▄███▓ ███▄ ▄███▓ ▄▄▄       ██▀███   ██ ▄█▀▓█████ ▒██   ██▒
    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▓█   ▀ ▒▒ █ █ ▒░
    ▓██    ▓██░▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒███   ░░  █   ░
    ▒██    ▒██ ▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ▒▓█  ▄  ░ █ █ ▒
    ▒██▒   ░██▒▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░▒████▒▒██▒ ▒██▒
    ░ ▒░   ░  ░░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░░ ▒░ ░▒▒ ░ ░▓ ░
    ░  ░      ░░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░ ░ ░  ░░░   ░▒ ░
    ░      ░   ░      ░     ░   ▒     ░░   ░ ░ ░░ ░    ░    ░    ░
           ░          ░         ░  ░   ░     ░  ░      ░  ░ ░    ░

    """
    print(accent_color + awesome_name)

    # The user has to select an option

    print(accent_color + "[0]" + text_color + " Full system upgrade")
    print(accent_color + "[1]" + text_color + " Social networks")
    print(accent_color + "[2]" + text_color + " News")
    print(accent_color + "[3]" + text_color + " Random wallpaper! (Pictures/Wallpapers/)")
    print(accent_color + "[4]" + text_color + " Github repositories")
    print(accent_color + "[5]" + text_color + " System options")
    print(accent_color + "\n[99]" + text_color + " Cancel\n")


    user_command = int(input(coloblue_input))


    if user_command == 0: # Realizes a system update and full-upgrade in Debian based distros

        os.system("sudo apt-get update && sudo apt-get full-upgrade && sudo apt autoremove && sudo apt clean")


    elif user_command == 1: # Opens social networks websites

        webbrowser.open_new_tab("http://manumercado.tk")
        time.sleep(1)
        webbrowser.open_new_tab("https://imgur.com")
        time.sleep(1)
        webbrowser.open_new_tab("https://instagram.com")
        time.sleep(1)
        webbrowser.open_new_tab("https://bluedit.com")
        time.sleep(1)
        webbrowser.open_new_tab("https://tumblr.com")
        time.sleep(1)
        webbrowser.open_new_tab("https://twitter.com")

        sys.exit(0)


    elif user_command == 2: # Opens news websites

        webbrowser.open_new_tab("https://engadget.com")
        time.sleep(1)
        webbrowser.open_new_tab("https://myki.com/blog")
        time.sleep(1)
        webbrowser.open_new_tab("https://nytimes.com/section/science")
        time.sleep(1)
        webbrowser.open_new_tab("https://nytimes.com/section/technology")
        time.sleep(1)
        webbrowser.open_new_tab("https://techcrunch.com")
        time.sleep(1)
        webbrowser.open_new_tab("https://thehackernews.com")
        time.sleep(1)
        webbrowser.open_new_tab("https://wsj.com/news/technology")

        sys.exit(0)


    elif user_command == 3: # Random wallpaper

        # Scans and print the directories inside '~/Pictures/Wallpapers' as a list

        directories = sorted(os.listdir("/home/mm4rk3t/Pictures/Wallpapers"))

        print(accent_color +"\n".join(directories)+"\n" + text_color)

        directory = input(coloblue_input)

        wallpaper = random.choice(os.listdir("/home/mm4rk3t/Pictures/Wallpapers/"+directory))
        os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/mm4rk3t/Pictures/Wallpapers/%s/%s" %(directory, wallpaper))


    elif user_command == 4: # Opens my Github repositories

        webbrowser.open_new_tab('https://github.com/mm4rk3t?tab=repositories')


    elif user_command == 5: # Displays some options

        def options():

            poweroff =  accent_color + "(P)" + text_color + "ower Off" + ", "
            reboot =    accent_color + "(R)" + text_color + "eboot" + ", "
            lock =      accent_color + "(L)" + text_color + "ock" + ", "
            suspend =   accent_color + "(S)" + text_color + "uspend" + ", "
            cancel =    accent_color + "(C)" + text_color + "ancel"

            print("\n" + poweroff + reboot + lock + suspend + cancel + "\n")

            sys_option = input(coloblue_input).lower()

            if sys_option == "p":
                os.system("poweroff")
            elif sys_option == "r":
                os.system("reboot")
            elif sys_option == "l":
                os.system("dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock")
            elif sys_option == "s":
                os.system("systemctl suspend")
            elif sys_option == "c":
                main()
            else:
                options()
        options()


    elif  user_command == 99:
        sys.exit(0)

colors.init()
main()
