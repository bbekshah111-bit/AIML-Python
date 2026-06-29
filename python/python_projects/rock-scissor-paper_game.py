import random

user_won = 0
computer_won = 0
options = ['rock', 'paper', 'scissor']

while True :
    user_input = input("Enter rock/paper/scissor or q to quit : ").lower()
    
    if user_input == 'q':
        print('okay, game quit!')
        break

    if user_input not in options :
        continue

    random_num = random.randint(0, 2)
    computer_guess = options[random_num]
    print(f'computer picked : {computer_guess}')

    if user_input == computer_guess :
        print('its a tie.')

    elif user_input == 'paper' and computer_guess == 'rock' :
        print('you won!') 
        user_won += 1

    elif user_input == 'rock' and computer_guess == 'scissor' :
        print('you won!')
        user_won += 1

    elif user_input == 'scissor' and computer_guess == 'paper' :
        print('you won!')
        user_won += 1

    else :
        print('computer won!')
        computer_won += 1
        

print(f'you won {user_won} times')
print(f'computer won {computer_won} times')
if user_won > computer_won :
    print('overall, you won!')

elif user_won == computer_won :
    print("Game tied!")

else :
    print('overall, computer won!')