import random
def main():
    print('=' * 40)
    print('Dice Rolling Game')
    print('=' * 40)
    MIN = 1
    MAX = 6

    again = 'y'
    while again == 'y' or again == 'Y':
        input('Roll the dice (click enter): ')
        print(random.randint(1, 6))
        again = input('Do you want to roll the dice again? (y / n): ')
        

if __name__ == '__main__':
    main()
