#import random library
import random 

#include wins and lose variables
wins = 0
loss = 0

#include a while loop 1st
while True:
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    #pass the possible choices in an array
    possible_choice = ["rock", "paper", "scissors"]
    #select computer choices using the random method
    computer_choice = random.choice(possible_choice)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n") #use string formatter or formatterstring literal

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            wins += 1
            print("Rock smashes scissors! You win!")
        else:
            loss += 1
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            loss += 1
            print("Paper covers rock! You win!")
        else:
            loss += 1
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            wins += 1
            print("Scissors cuts paper! You win!")
        else:
            loss += 1
            print("Rock smashes scissors! You lose.")
    

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    print(f"\n You won {wins} times and lost {loss} times\n")


print("Thanks for playing :) ")
print(f"\n You won {wins} times and lost {loss} times\n")


