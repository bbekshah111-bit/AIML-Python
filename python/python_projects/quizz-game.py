#creating quizz game using if else conditions

print('welcome to my computer quizz')
playing = input("Do you want to play? \n1.yes\n2.no\n ->")
if playing.lower() == "yes":
 print("okay! let's play :)")  
elif playing == '1' :
    print("okay! let's play :)")
elif playing.lower() == "no":
    print("okay! game exited")
    quit()
elif playing == '2' :
    print("okay! game exited")
    quit()
else :
    print("invalid input")
    quit()
score = 0 
answer = input("what does CPU stand for? : ")
if answer.lower() == "central processing unit":
    print("correct guess!")
    score += 1
else :
    print("you are wrong")


answer = input("what does GPU stand for? : ")
if answer.lower() == "graphics processing unit":
    print("correct guess!")
    score += 1
else :
    print("you are wrong")


answer = input("what does ML stand for? : ")
if answer.lower() == "mechine learning":
    print("correct guess!")
    score += 1
else :
    print("you are wrong")


answer = input("what does DSA stand for? : ")
if answer.lower() == "data structure and algorithm":
    print("correct guess!")
    score += 1
else :
    print("you are wrong")

print(f"you made {score} questions correct.")
print(f"you got {(score/4)*100}%")