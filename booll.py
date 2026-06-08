'''
Write a program that predicts the approximate size of a population of organisms. The  
application should use text boxes to allow the user to enter the starting number of organisms,
the average daily population increase (as a percentage), and the number of days the 
organisms will be left to multiply. For example, assume the user enters the following values:
Starting number of organisms: 2
Average daily increase: 30%
Number of days to multiply: 10
The program should display the following table of data:
Day Approximate                Population
1
2
3
4
5
6
7
8
9
10

'''

def main():
    input("Press Enter to start the game...")  # waits until Enter is pressed
    start_game()
    start = int(input('Starting number of the organisms: '))
    daily_increase = float(input('Average daily increase (%): '))
    num_days = int(input('Number of days to multiply: '))

    perc = daily_increase / 100
    population = start
    
    print("Day\tApproximate Population")
    for day in range(1, num_days + 1):
        print(f"{day}\t{population:.2f}")
        population += population * perc 
    

def start_game():
    print("🎮 Game has started! Let’s go...")




if __name__ == '__main__':
    main()
