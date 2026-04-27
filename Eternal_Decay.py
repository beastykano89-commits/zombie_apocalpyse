'''
rules:
1. Break statements not allowed
2. Max num of 7 learners allowed.
must have a min of 7 functions
'''
def main():

    intro()
    name = input('Enter your [ NAME ] survivor: ')
    intro_menu()
    start = int(input('[SYSTEM]: Input "1" to engage survival mode:'))
    start_menu(start)

    options()
    noise = input('Investigate the noise (y/n)? ')
    while noise != 'y'  and noise != 'n':
        noise = input('Respond (y) or (n): ')

    dash = None
    tools = None
    what = None
    wake = None
    run = None
    choice = None
    final = None

    if noise == 'y':
        print('\nYou look out your room...\nA massive horde is rushing toward you!')
        print('Judging by the eerie noise, inhumane')
        
        print('\n 1 - Staircase')
        print('\n 2 - Hospital Window')
        print('\n 3 - Hold the door')
        dash = int(input('What do you do? '))
        while dash != 1 and dash != 2 and dash != 3:
            print('\n 1 - Staircase')
            print('\n 2 - Hospital Window')
            print('\n 3 - Hold the door')
            dash = int(input('Action (1 - 3): '))


        if dash == 1:
            print('\nYou are in a dangerous zone, Zombies roaming around.')
            print('You make way to the hall, The silence is deaffening')
            print('Flickering Lights...')
            print('Dark stain on the walls...')
            print('Dragging footsteps creep closer')
            
            print('\n[WARNING]: Hallway compromised. Shadows are shifting.')
            print('\n1 - Move through the shadows, down the hall')
            print('2 - Attempt rooftop path')

            run = int(input('[INPUT] Select 1 or 2: '))
            while run != 1 and run != 2:
                run = int(input('[INPUT] Select 1 or 2: '))

            if run == 1:
                print('You move slower, controlled breathing. A Zombie...')
                print('But - It can not see.')
                print('\nA Broken wall, there on a loose map.')
                
              #  print('\n"ROME"') 
                draw_rome()       
                print('All infected are converging on these coordinates.')
                print('\nClose by: a staircase')
                print('2 - Attempt rooftop path')
                print('\n1 - Move through the shadows, down the hall')
                choice = int(input('[INPUT] Select 1 or 2: '))
                while choice != 1 and choice != 2:
                    choice = int(input('[INPUT] Select 1 or 2: '))

                if choice == 1:
                    print('Your body, weak but you manage the flight of stairs.')
                    print('The Rooftop:')
                    print('[COMM]: Helicopter in range! You have been spotted.')
                    print('A soldier drops a tether.')
                    print('\nHordes are breaching the roof access!')
                    print('1 - Grab the tether immediately')
                    print('2 - Hold position and fight')
                    final = int(input('[INPUT]: Select 1 or 2: '))
                    while final != 1 and final != 2:
                        final = int(input('[INPUT]: Select 1 or 2: '))

                    if final == 1:
                        print(f'\n[MISSION SUCCESS]: Tether secured. You are extracted, {name}. You live.')
                    elif final == 2:
                        print('\n[CRITICAL]: The horde is too dense. You are overrun.')
                        print('[LOG]: Helicopter departing. Abandoned.')
                        print('[MISSION FAILED]')
                        return
                
                elif choice == 2:
                    print('[WARNING!]Spotted by infected.')
                    print('You Are BITTEN >> [FATAL]')
                    print('[MISSION FAILED]')
                    return
                
            elif run == 2:
                print('Your body, weak but you manage the flight of stairs.')
                print('The Rooftop:')
                print('[COMM]: Helicopter in range! You have been spotted.')
                print('A soldier drops a tether.')
                print('\nHordes are breaching the roof access!')
                print('A rope drops')
                print('1 - Grab the tether immediately')
                print('2 - Hold position and fight')


                final = int(input('[INPUT]: Select 1 or 2: '))
                while final != 1 and final != 2:
                    final = int(input('[INPUT]: Select 1 or 2: '))

                if final == 1:
                    print(f'\n[MISSION SUCCESS]: Tether secured. You are extracted, {name}. You live.')

                elif final == 2:
                    print('[WARNING!]Spotted by infected.')
                    print('You Are BITTEN >> [FATAL]')
                    print('[MISSION FAILED]')
                    

        elif dash == 2:
            print('\n[INJURED]: Fall impact lethal. Internal hemorrhaging.')
            print('[FATAL]: You were devoured.')
            print('[MISSION FAILED]')
            return
            
        elif dash == 3:
            print('\n[FATAL]: The door buckled. You were devoured.')
            print('[MISSION FAILED]')
            return
        
    elif noise == 'no':
        print('[WEAPON]: surgical scalpal')
        print('[ITEMS]: To your right - CellPhone, Grenade [+- 20 years], Medical kit..')

        what = input('Take items (y)/(n)')
        while what != 'y' and what != 'n':
            what = input('Respond (y) or (n): ')

        if what == 'y':
            tools = input('[ITEM TAKEN]:((p)hone/(g)renade/(m)edical kit/(s)calpel)?: ')
            while tools != 'p' and tools != 'g' and tools != 'm' and tools != 's':
                print('ONLY ((p)hone, (g)renade, (m)edical kit or (s)calpal)')
                tools = input('[SPECIFY ITEM TAKEN]: ')

            if tools == 'p':
                print('CellPhone Broken.')

            elif tools == 'g':
                print('[WEAPON ADDED TO INVENTORY]')

            elif tools == 'med kit':
                print('[MEDICAL KIT ADDED TO INVENTORY]')

            elif tools == 'scalpel':
                print('[WEAPON ADDED TO INVENTORY]')

            print('\n 1 - Staircase')
            print('\n 2 - Hospital Window')
            print('\n 3 - Hold the door')
            dash = int(input('What do you do? '))
            while dash != 1 and dash != 2 and dash != 3:
                dash = int(input('Action (1 - 3): '))

            if dash == 1:
                print('\nYou are in a dangerous zone, Zombies roaming around.')
                print('You make way to the hall, The silence is deaffening')
                print('Flickering Lights...')
                print('Dark stain on the walls...')
                print('Dragging footsteps creep closer')
                
                print('\n[WARNING]: Hallway compromised. Shadows are shifting.')
                print('\n1 - Move through the shadows, down the hall')
                print('2 - Attempt rooftop path')

                run = int(input('[INPUT] Select 1 or 2: '))
                while run != 1 and run != 2:
                    run = int(input('[INPUT] Select 1 or 2: '))

                if run == 1:
                    print('You move slower, controlled breathing. A Zombie...')
                    print('But - It can not see.')
                    print('\nA Broken wall, there on a loose map.')
                    
                    #print('\n"ROME"')
                    draw_rome()
                    print('All infected are converging on these coordinates.')
                    print('\nClose by: a staircase')
                    print('2 - Attempt rooftop path')
                    print('\n1 - Move through the shadows, down the hall')
                    choice = int(input('[INPUT] Select 1 or 2: '))
                    while choice != 1 and choice != 2:
                        choice = int(input('[INPUT] Select 1 or 2: '))

                    if choice == 1:
                        print('Your body, weak but you manage the flight of stairs.')
                        print('The Rooftop:')
                        print('[COMM]: Helicopter in range! You have been spotted.')
                        print('A soldier drops a tether.')
                        print('\nHordes are breaching the roof access!')
                        print('A rope drops')
                        print('1 - Grab the tether immediately')
                        print('2 - Hold position and fight')
                        
                        final = int(input('[INPUT]: Select 1 or 2: '))
                        while final != 1 and final != 2:
                            final = int(input('[INPUT]: Select 1 or 2: '))

                        if final == 1:
                            print(f'\n[MISSION SUCCESS]: Tether secured. You are extracted, {name}. You live.')
                        elif final == 2:
                            print('\n[CRITICAL]: The horde is too dense. You are overrun.')
                            print('[LOG]: Helicopter departing. Abandoned.')
                            print('[MISSION FAILED]')
                            return
                            
                    elif choice == 2:
                        print('[WARNING!]Spotted by infected.')
                        print('You Are BITTEN >> [FATAL]')
                        print('[MISSION FAILED]')
                        return
                    
                elif run == 2:
                    print('Your body, weak but you manage the flight of stairs.')
                    print('The Rooftop:')
                    print('[COMM]: Helicopter in range! You have been spotted.')
                    print('A soldier drops a tether.')
                    print('\nHordes are breaching the roof access!')
                    print('A rope drops')
                    print('1 - Grab the tether immediately')
                    print('2 - Hold position and fight')
                
                    final = int(input('[INPUT]: Select 1 or 2: '))
                    while final != 1 and final != 2:
                        final = int(input('[INPUT]: Select 1 or 2: '))

                    if final == 1:
                        print(f'\n[MISSION SUCCESS]: Tether secured. You are extracted, {name}. You live.')

                    elif final == 2:
                        print('\n[CRITICAL]: The horde is too dense. You are overrun.')
                        print('[LOG]: Helicopter departing. Abandoned.')
                        print('[MISSION FAILED]')
                        return
                        
                    elif dash == 2:
                        print('\n[INJURED]: Fall impact lethal. Internal hemorrhaging.')
                        print('[FATAL]: You were devoured.')
                        print('[MISSION FAILED]')
                    elif dash == 3:
                        print('\n[FATAL]: The door buckled. You were devoured.')
                        print('[MISSION FAILED]')


        elif what == 'no':
            print('You body is weak, vitals are low.')
            print('1 - Scavange food')
            print('2 - Rest')

            wake = int(input('[INPUT]: Select 1 or 2: '))
            while wake != 1 and wake != 2:
                print('You body is weak, vitals are low.')
                print('1 - Scavange food')
                print('2 - Rest')
                wake = int(input('[INPUT]: Select 1 or 2: '))

            if wake == 1:
                print('Food item available : Canned Spagetthi')
                food = input('Do you eat it (y/n)? ')
                while food != 'y' and food != 'n':
                    food = input('Respond (y) or(n): ')
                
                if food == 'y':
                    print('[EXPIRED FOOD]: Fatal death by food poisoning')
                    print('[MISSION FAILED]')
                    return
                   
                elif food == 'no':
                    print('\n[FATAL]: Starvation')
                    print('[MISSION FAILED]')
                    return
                    

            elif wake == 2:
                print('\n[FATAL]: Starvation')
                print('[MISSION FAILED]')
                return
            

def intro():
    print('=' * 65)
    print('                    [ETERNAL DECAY ]                     ')
    print('       ALL ZOMBIES LEAD TO ROME: SURVIVAL PROTOCOL       ')
    print('=' * 65)


def intro_menu():
    print('\nYou awaken alone in a broken world where silence is more')
    print('terrifying than screams. The air carries the stench of decay.')
    print('Chaos waits—hungry, patient, and much closer than you think.')
    
def start_menu(start):
    found = False
    while found:
        start = int(input('[SYSTEM]: Input "1" to engage survival mode: '))
        if start == 1:
            found = True
        else:
            start = int(input('[SYSTEM]: Input "1" to engage survival mode: '))
            
    return start

def options():
    print('\n[STATUS]:  20 Year Cryo-Coma ended. obscured. Hospital bed.')
    print('[ALERT]: Flickering lights above. An eerie, wet thud sounds nearby.')

def draw_rome():
    print("""
██████╗  ██████╗ ███╗   ███╗███████╗
██╔══██╗██╔═══██╗████╗ ████║██╔════╝
██████╔╝██║   ██║██╔████╔██║█████╗  
██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝  
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
    """)
    print('    [DATA LOG]: All infected are converging on these coordinates.')

if __name__== '__main__':
    main()
