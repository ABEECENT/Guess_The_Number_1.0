def menu():
    print('< < < WELCOME TO GUESS THE NUMBER > > >'+'\n')
    print('[1] 1 Player')
    print('[2] 2 Players')
    print('[3] 3 Players')
    print('[4] 4 Players')
    print('[0] EXIT'+'\n')

    choice=input('Pick the number ==> ')

    return int(choice)

def menu_check(option):
    if option not in [1,2,3,4,0]:
        return False
    else:
        return True
