import random
from rand_num import generate_number
from hint import get_hint
def guess_num():
    number = generate_number()
    attempts = 6
    
    while True:
      
        guess = input(f"{attempts} attempts left. Type a number to guess or press H for a hint: ")        
        try:
            
            if guess.lower() == "h":
                attempts -= 1
                get_hint()
    
            if guess.lower() == "q":
                print("You try to run, but you trip, kick the table, and the sudden jolt sets off the bomb!")
                break
            if attempts < 1:
                print("The bomb goes off! You see a bright flash, then nothing. Game Over.")
                break
            else:
            
                guess = int(guess)
                
                if number < guess:
                    attempts -= 1
                    print(f"You have a hunch that the number lower than {guess}")
                    print("")                    

                if number > guess:
                    attempts -= 1
                    print(f"you have a hunch that the number is higher than {guess}")
                    print("")
                    
                
                if number == guess:
                    print(f"You did it! You disarmed the bomb!")
                    break

                if attempts < 1:
                    print("The bomb goes off! You see a bright flash, then nothing. Game Over.")
                    break
                
        except ValueError as e:
            if guess.lower() == "h":
                continue
            print("Invalid input.")
            print("")