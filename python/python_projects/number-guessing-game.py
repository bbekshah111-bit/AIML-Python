import random
"""random is a built_in module that allows us to use random.rand or random.randint 
 to print random number in certain range"""

#took input for certain range
certain_range = input("enter certain number : ")

#checked whether input is valid integer or not, if not re-enter the number again
#if yes convert it into integer through int
if certain_range.isdigit():
    certain_range = int(certain_range)
    if certain_range <= 0:
        print(" invalid! enter number above 0 next time")
        quit()
else :
    print("error! enter a number next time")

#used random module to print random number using user input above i.e certain_range
random_num = random.randint(0, certain_range)

#used while loop to create certain condition so the loop will continue until the user inputs correct number
score = 0
while True:
    score += 1
    user_guess = input("guess the number : ")
    
    #again checked whether input is valid or not
    if user_guess.isdigit():
       user_guess = int(user_guess)
    else :
      print("error! enter a number next time")
      continue
    ##checked if user inpute is correct or not to random number,
    ##using break, if correct to get out of loop
    if user_guess == random_num :
        print("you got it!")
        print(f"you got it in {score} chances")
        break
    else :
        print('you get it wrong')
    
    if user_guess < random_num:
        print("it is above this number")

    else :
        print("it is below this number")





