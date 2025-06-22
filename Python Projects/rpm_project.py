import random as rd

class RPM(object):
    # taking inputs
    def get_choices(self):
        p_choice = input("Enter your choice from: ['Rock', 'Paper', 'Scissors']: ")
        choices = ['Rock', 'Paper', 'Scissors']
        comp_choice = rd.choice(choices)
        print(f"Computer's choice: {comp_choice}")
        
        final_choices = {'Player': p_choice.capitalize(), 'Computer': comp_choice}
        return final_choices
    
    def check_win(self, player, computer):
        print(f"You chose {player}, computer chose {computer}")
        if player == computer:
            return "It's a tie!"
        elif player == "Rock":
            if computer == "Scissors":
                return "Rock smashes scissors! You win!"
            else:
                return "Paper covers rock! You lose."
        elif player == "Paper":
            if computer == "Rock":
                return "Paper covers rock! You win!"
            else:
                return "Scissors cuts paper! You lose."
        elif player == "Scissors":
            if computer == "Paper":
                return "Scissors cuts paper! You win!"
            else:
                return "Rock smashes scissors! You lose."

# Instantiate the class and play
rpm = RPM()
choices = rpm.get_choices()
result = rpm.check_win(choices["Player"], choices["Computer"])
print(result)
