# Hi!

<b>mmarkex</b> is a tool that I coded in order to save some time or
just have fun. In the way I coded it, unfortunately some options are only
available in Debian-based distros, which, in my case, is Ubuntu 18.04.2 LTS.

If you use this tool, please give me some feedback, it will help to make it
better ;)

## Libraries used:
- fileinput
- os (also import sys from os)
- random
- time
- webbrowser

Some of these libraries are already installed by default, but you will have to install the ones which are not in order to run the program without any troubles.

It is very important to keep the files in the same directory, otherwise, 'changeColors.py' will be useless, so will be 'colors.py'.

If you want to run <b>mmarkex</b> without the need of going to the
directory,you will have to edit 'makeBin.sh' and run it as superuser. In my case it would be:

`sudo echo "python3 /home/mm4rk3t/Github/mmarkex/mmarkex.py" >> /usr/bin/mmarkex && sudo chmod +x /usr/bin/mmarkex`

Then you give it executable permission

`sudo chmod +x makeBin.sh`

And you run it

`sudo ./makeBin.sh`


That's all you have to do, here you have a screenshot:

![Image](img/screenshot.png?raw=true)

Feel free to modify it in order to suit your needs, as it is suited for mine.

If you detect any bugs or have any recommendations, please [email
me](mailto:mercadomanuu@outlook.com). I will gladly take your critics into account.

Also, check out my (http://manumercado.tk)[website]

Enjoy your day!


_Tested in python 3.6.7_
