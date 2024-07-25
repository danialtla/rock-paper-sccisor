import random
import time

def replaceStr(choose):
    # Print the AI's choice
    options = ['Rock', 'Paper', 'Scissor']
    print(f"The A.I. picks {options[choose]}")

def determine_winner(user_pick, ai_pick):
    # Determine the winner
    if (user_pick == 'r' and ai_pick == 's') or \
       (user_pick == 'p' and ai_pick == 'r') or \
       (user_pick == 's' and ai_pick == 'p'):
        return "You win!"
    elif user_pick == ai_pick:
        return "It's a tie. Try again."
    else:
        return "A.I. wins!"

def main():
    # Main game loop
    user_play = input("Do you want to play rock-paper-scissors? [y/n] ").lower()
    ai_option_list = ['r', 'p', 's']

    while user_play in ['yes', 'y']:
        user_pick = input("Pick 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
        ai_pick = random.choice(ai_option_list)
        ai_choose = ai_option_list.index(ai_pick)

        replaceStr(ai_choose)
        time.sleep(1)
        result = determine_winner(user_pick, ai_pick)
        print(result)

        time.sleep(1)
        user_play = input("Do you want to play again? [y/n] ").lower()

    print("Thank you for playing this game!")

if __name__ == "__main__":
    main()

