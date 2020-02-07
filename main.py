# Guess the number game

# modules

import start
import game

# from modules

from start import *

from game import *

# loop

opt=1

while(opt!=0):
    opt=menu()
    print()

    check=menu_check(opt)

    while(check==False):
        print('Please Try Again !!!')
        opt=menu()
        print()
        check=menu_check(opt)

    if(opt==1):
        oneplayer()
        print()
    elif(opt==2):
        twoplayer()
        print()
    elif(opt==3):
        threeplayer()
        print()
    elif(opt==4):
        fourplayer()
        print()
    else:
        print('Thank You For Playing The Game :D')
