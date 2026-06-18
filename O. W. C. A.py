# Kano, Mokwena
'''
Rules: there can only be Agent P or Major F else BOOM!
'''
import math
import random
import time
import sys


# Define the main function
def main():
    print('='*45)
    print('O.W.C.A')
    print('Organization Without a Cool Acronym')
    print('='*45)

    # The user must enter either Agent P or Major F for this program to commence
    NameID = input('Please enter the code name: ')
    if NameID == 'Agent P':
        print('-'*45)
        print('Welcome Perry the Platypus to O.W.C.A')
        print('You have  Level 1 Clearance.\n')
        print('-'*45)

        choice = None
        while choice != 0:
            menu1()
            choice = int(input('Option: '))
            if choice == 1:
                again = 'y'
                while again == 'y' or again == 'Y':
                    message = input('Encode a message: ')
                    encode(message)
                    again = input('Would you like to continue(y / n): ')
            elif choice == 2:
                blast_rad()
            elif choice == 0:
                print('You have exited the program. Goodbye!')
            else:
                print('No options have been selected')

    
    elif NameID == 'Major F':
        print('-'*45)
        print('Welcome Major Francis Monogram to O.W.C.A')
        print('You have  Level 2 Clearance.\n')
        print('-'*45)

        choice = None
        while choice != 0:
            menu2()
            choice = int(input('Option: '))
            if choice == 1:
                again = 'y'
                while again == 'y' or again == 'Y':
                    message = input('Encode a message: ')
                    encode(message)
                    again = input('Would you like to continue(y / n): ')
            elif choice == 2:
                blast_rad()
            elif choice == 3:
                password()
            elif choice == 0:
                print('You have exited the program. Goodbye!')
            else:
                print('No options have been selected')

    elif NameID =='':
        print('Nothing was inserted.')

    else:
        print('ACCESS DENIED...SELF DESTRUCION IN...')
        explode = ['3...', '2...', '1...', 'BOOM']
        delays = [0.9, 0.9, 0.9, 0.9]

        for x, line in enumerate(explode):
            for y in line:
                sys.stdout.write(y)
                sys.stdout.flush()
            print()
            time.sleep(delays[x])
            
        
# Menu
def menu1():
    print('-'*45)
    print('Please choose one of the following options:')
    print('-'*45)
    print('0. Exit')
    print('1. Encode a message.')
    print('2. Determine blast radius.')


# Menu
def menu2():
    print('-'*45)
    print('Please choose one of the following options:')
    print('-'*45)
    print('0. Exit')
    print('1. Encode a message.')
    print('2. Determine blast radius.')
    print('3. Generate a password.')
    

# This function is for replacing the vowels in the message the user enters for example: kano = k*n*
def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ''
    for x in message:
        if x.lower() in vowels:
            encoded += '*'
        else:
            encoded += x
    print(f'Enoded message: {encoded}')


# This function is for when the user is not recognised. in such case a bomb is activated
def blast_rad():
    size = float(input('Enter the bomb size: '))
    blast = (size)**2 * (math.pi)
    print(f'The calculated blast radius is: {blast:.2f}')


# This function is for creating a random paswword based on the length the user inputs                
def password():
    again = 'y'
    while again.lower() == 'y':
        word = int(input('Please enter the password length: '))
        password = ''
        for x in range(word):
            password += str(random.randint(0, 9))
        print(f'New password: {password}')
        again = input('Would you like to continue(y / n): ')


if __name__ == '__main__':
    main()
