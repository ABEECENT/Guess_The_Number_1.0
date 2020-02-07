# Modules

import random

# For one player

def oneplayer():

    print('< < < INSTRUCTIONS > > >'+'\n')
    print('1. The computer will generate the number from 0 to 20 inclusive.')
    print('2. You will be given 3 tries')
    print('3. After answering, you will receive a Description of the distance')
    print('   between your number and the generated number. The Hotter the   ')
    print('   Description P1, the closer you are to the number.'+'\n')
    print('To return to the title screen, enter -1 '+'\n')

    guess=1
    max=20

    while(guess!=-1):

        cpu=random.randint(0,max)

        print('A number has been generated! Good Luck!'+'\n')

        i=0

        for i in range(3):

            guess=int(input('Guess '+str(i+1)+' ==> '))

            while guess not in range(-1,max+1):
                print('Please Try Again !!!')
                guess=int(input('Guess '+str(i+1)+' ==> '))
                print()

            if(guess==-1):
                break

            if(guess==cpu):
                print('That is a correct guess you win !!'+'\n')
                break
            elif(abs(guess-cpu)>round(0.5*max)):
                print('Description P1: Cold'+'\n')
            elif(abs(guess-cpu)<=round(0.5*max) and abs(guess-cpu)>round(0.25*max)):
                print('Description P1: Warm'+'\n')
            elif(abs(guess-cpu)<=round(0.25*max) and abs(guess-cpu)>round(0.10*max)):
                print('Description P1: Hot'+'\n')
            elif(abs(guess-cpu)<=round(0.10*max)):
                print('Description P1: RED HOT, RED HOT!!!'+'\n')

            i+=1

            if(i==3):
                print('Tough Luck! But the correct number is '+ str(cpu)+' !'+'\n')

        if(guess==-1):
            break

# for 2 players

def twoplayer():
    print('< < < INSTRUCTIONS > > >'+'\n')
    print('1. The computer will generate the number from 0 to 40 inclusive.')
    print('2. Each of you will be given 3 tries')
    print('3. After answering, each of you will receive a Description of the distance')
    print('   between your number and the generated number. The Hotter the   ')
    print('   Description P1, the closer you are to the number.'+'\n')
    print('To return to the title screen, enter -1 '+'\n')

    guess1=1
    guess2=1
    max=40

    while(guess1!=-1 or guess2!=-1):
        cpu=random.randint(0,max)

        print('A number has been generated! Good Luck!'+'\n')

        i=0

        for i in range(3):

            guess1=int(input('Player 1 Guess '+str(i+1)+' ==> '))

            while guess1 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess1=int(input('Player 1 Guess '+str(i+1)+' ==> '))
                print()

            if(guess1==-1):
                break

            guess2=int(input('Player 2 Guess '+str(i+1)+' ==> '))

            while guess2 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess2=int(input('Player 2 Guess '+str(i+1)+' ==> '))
                print()

            if(guess2==-1):
                break

            if(guess1==cpu):
                print('That is a correct guess, Player 1 you win !!'+'\n')
                break
            elif(abs(guess1-cpu)>round(0.5*max)):
                print('Description P1: Cold'+'\n')
            elif(abs(guess1-cpu)<=round(0.5*max) and abs(guess1-cpu)>round(0.25*max)):
                print('Description P1: Warm'+'\n')
            elif(abs(guess1-cpu)<=round(0.25*max) and abs(guess1-cpu)>round(0.10*max)):
                print('Description P1: Hot'+'\n')
            elif(abs(guess1-cpu)<=round(0.10*max)):
                print('Description P1: RED HOT, RED HOT!!!'+'\n')

            if(guess2==cpu):
                print('That is a correct guess, Player 2 you win !!'+'\n')
                break
            elif(abs(guess2-cpu)>round(0.5*max)):
                print('Description P2: Cold'+'\n')
            elif(abs(guess2-cpu)<=round(0.5*max) and abs(guess2-cpu)>round(0.25*max)):
                print('Description P2: Warm'+'\n')
            elif(abs(guess2-cpu)<=round(0.25*max) and abs(guess2-cpu)>round(0.10*max)):
                print('Description P2: Hot'+'\n')
            elif(abs(guess2-cpu)<=round(0.10*max)):
                print('Description P2: RED HOT, RED HOT!!!'+'\n')

            i+=1

            if(i==3):
                print('Tough Luck! But the correct number is '+ str(cpu)+' !'+'\n')

        if(guess1==-1):
            break

        if(guess2==-1):
            break


def threeplayer():
    print('< < < INSTRUCTIONS > > >'+'\n')
    print('1. The computer will generate the number from 0 to 50 inclusive.')
    print('2. Each of you will be given 3 tries')
    print('3. After answering, each of you will receive a Description of the distance')
    print('   between your number and the generated number. The Hotter the   ')
    print('   Description P1, the closer you are to the number.'+'\n')
    print('To return to the title screen, enter -1 '+'\n')

    guess1=1
    guess2=1
    guess3=1
    max=50

    while(guess1!=-1 or guess2!=-1 or guess3!=-1):
        cpu=random.randint(0,max)

        print('A number has been generated! Good Luck!'+'\n')

        i=0

        for i in range(3):

            guess1=int(input('Player 1 Guess '+str(i+1)+' ==> '))

            while guess1 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess1=int(input('Player 1 Guess '+str(i+1)+' ==> '))
                print()

            if(guess1==-1):
                break

            guess2=int(input('Player 2 Guess '+str(i+1)+' ==> '))

            while guess2 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess2=int(input('Player 2 Guess '+str(i+1)+' ==> '))
                print()

            if(guess2==-1):
                break

            guess3=int(input('Player 3 Guess '+str(i+1)+' ==> '))

            while guess3 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess3=int(input('Player 3 Guess '+str(i+1)+' ==> '))
                print()

            if(guess3==-1):
                break


            if(guess1==cpu):
                print('That is a correct guess, Player 1 you win !!'+'\n')
                break
            elif(abs(guess1-cpu)>round(0.5*max)):
                print('Description P1: Cold'+'\n')
            elif(abs(guess1-cpu)<=round(0.5*max) and abs(guess1-cpu)>round(0.25*max)):
                print('Description P1: Warm'+'\n')
            elif(abs(guess1-cpu)<=round(0.25*max) and abs(guess1-cpu)>round(0.10*max)):
                print('Description P1: Hot'+'\n')
            elif(abs(guess1-cpu)<=round(0.10*max)):
                print('Description P1: RED HOT, RED HOT!!!'+'\n')

            if(guess2==cpu):
                print('That is a correct guess, Player 2 you win !!'+'\n')
                break
            elif(abs(guess2-cpu)>round(0.5*max)):
                print('Description P2: Cold'+'\n')
            elif(abs(guess2-cpu)<=round(0.5*max) and abs(guess2-cpu)>round(0.25*max)):
                print('Description P2: Warm'+'\n')
            elif(abs(guess2-cpu)<=round(0.25*max) and abs(guess2-cpu)>round(0.10*max)):
                print('Description P2: Hot'+'\n')
            elif(abs(guess2-cpu)<=round(0.10*max)):
                print('Description P2: RED HOT, RED HOT!!!'+'\n')

            if(guess3==cpu):
                print('That is a correct guess, Player 3 you win !!'+'\n')
                break
            elif(abs(guess3-cpu)>round(0.5*max)):
                print('Description P2: Cold'+'\n')
            elif(abs(guess3-cpu)<=round(0.5*max) and abs(guess3-cpu)>round(0.25*max)):
                print('Description P2: Warm'+'\n')
            elif(abs(guess3-cpu)<=round(0.25*max) and abs(guess3-cpu)>round(0.10*max)):
                print('Description P2: Hot'+'\n')
            elif(abs(guess3-cpu)<=round(0.10*max)):
                print('Description P2: RED HOT, RED HOT!!!'+'\n')

            i+=1

            if(i==3):
                print('Tough Luck! But the correct number is '+ str(cpu)+' !'+'\n')

        if(guess1==-1):
            break

        if(guess2==-1):
            break

        if(guess3==-1):
            break

def fourplayer():
    print('< < < INSTRUCTIONS > > >'+'\n')
    print('1. The computer will generate the number from 0 to 70 inclusive.')
    print('2. Each of you will be given 3 tries')
    print('3. After answering, each of you will receive a Description of the distance')
    print('   between your number and the generated number. The Hotter the   ')
    print('   Description P1, the closer you are to the number.'+'\n')
    print('To return to the title screen, enter -1 '+'\n')

    guess1=1
    guess2=1
    guess3=1
    guess4=1
    max=70

    while(guess1!=-1 or guess2!=-1 or guess3!=-1 or guess4!=-1):
        cpu=random.randint(0,max)

        print('A number has been generated! Good Luck!'+'\n')

        i=0

        for i in range(3):

            guess1=int(input('Player 1 Guess '+str(i+1)+' ==> '))

            while guess1 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess1=int(input('Player 1 Guess '+str(i+1)+' ==> '))
                print()

            if(guess1==-1):
                break

            guess2=int(input('Player 2 Guess '+str(i+1)+' ==> '))

            while guess2 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess2=int(input('Player 2 Guess '+str(i+1)+' ==> '))
                print()

            if(guess2==-1):
                break

            guess3=int(input('Player 3 Guess '+str(i+1)+' ==> '))

            while guess3 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess3=int(input('Player 3 Guess '+str(i+1)+' ==> '))
                print()

            if(guess3==-1):
                break

            guess4=int(input('Player 4 Guess '+str(i+1)+' ==> '))

            while guess4 not in range(-1,max+1):
                print('Please Try Again !!!')
                guess4=int(input('Player 4 Guess '+str(i+1)+' ==> '))
                print()

            if(guess4==-1):
                break


            if(guess1==cpu):
                print('That is a correct guess, Player 1 you win !!'+'\n')
                break
            elif(abs(guess1-cpu)>round(0.5*max)):
                print('Description P1: Cold'+'\n')
            elif(abs(guess1-cpu)<=round(0.5*max) and abs(guess1-cpu)>round(0.25*max)):
                print('Description P1: Warm'+'\n')
            elif(abs(guess1-cpu)<=round(0.25*max) and abs(guess1-cpu)>round(0.10*max)):
                print('Description P1: Hot'+'\n')
            elif(abs(guess1-cpu)<=round(0.10*max)):
                print('Description P1: RED HOT, RED HOT!!!'+'\n')

            if(guess2==cpu):
                print('That is a correct guess, Player 2 you win !!'+'\n')
                break
            elif(abs(guess2-cpu)>round(0.5*max)):
                print('Description P2: Cold'+'\n')
            elif(abs(guess2-cpu)<=round(0.5*max) and abs(guess2-cpu)>round(0.25*max)):
                print('Description P2: Warm'+'\n')
            elif(abs(guess2-cpu)<=round(0.25*max) and abs(guess2-cpu)>round(0.10*max)):
                print('Description P2: Hot'+'\n')
            elif(abs(guess2-cpu)<=round(0.10*max)):
                print('Description P2: RED HOT, RED HOT!!!'+'\n')

            if(guess3==cpu):
                print('That is a correct guess, Player 3 you win !!'+'\n')
                break
            elif(abs(guess3-cpu)>round(0.5*max)):
                print('Description P2: Cold'+'\n')
            elif(abs(guess3-cpu)<=round(0.5*max) and abs(guess3-cpu)>round(0.25*max)):
                print('Description P2: Warm'+'\n')
            elif(abs(guess3-cpu)<=round(0.25*max) and abs(guess3-cpu)>round(0.10*max)):
                print('Description P2: Hot'+'\n')
            elif(abs(guess3-cpu)<=round(0.10*max)):
                print('Description P2: RED HOT, RED HOT!!!'+'\n')

            if(guess4==cpu):
                print('That is a correct guess, Player 3 you win !!'+'\n')
                break
            elif(abs(guess4-cpu)>round(0.5*max)):
                print('Description P2: Cold'+'\n')
            elif(abs(guess4-cpu)<=round(0.5*max) and abs(guess4-cpu)>round(0.25*max)):
                print('Description P2: Warm'+'\n')
            elif(abs(guess4-cpu)<=round(0.25*max) and abs(guess4-cpu)>round(0.10*max)):
                print('Description P2: Hot'+'\n')
            elif(abs(guess4-cpu)<=round(0.10*max)):
                print('Description P2: RED HOT, RED HOT!!!'+'\n')


            i+=1

            if(i==3):
                print('Tough Luck! But the correct number is '+ str(cpu)+' !'+'\n')

        if(guess1==-1):
            break

        if(guess2==-1):
            break

        if(guess3==-1):
            break

        if(guess4==-1):
            break
