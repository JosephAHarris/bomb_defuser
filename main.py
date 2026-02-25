"""The purpose of this project is to create a "lockpick game" 
where you guess a number within a certain number of tries. 
This will be similar to Final Fantasy 11's chest opening minigame"""
from guess import guess_num

def main():
    print("There is a bomb on the table!")
    print("")
    print("The bomb can be disarmed by inputting the correct number from 10-99.")
    print("")
    print("You have 6 attempts before the bomb blows!")
    print("")
    guess_num()

main()