import random 

is_running = True 
counter = 1

print("------ Number Guessing Game -----")

secret_num = random.randint(1,100) # computer generates a random number
while is_running:
    user_input = int(input("Guess the number between 1 to 100\n"))
    if user_input<1 or user_input>100 :
        print("Invalid input! Given range should be considered! ")
        break

    if (secret_num == user_input):
        print("---- Congratulation You won ----")
        counter += 1  #For Game Count
        break
    else:
        print("You lose! ")

    choice = input("Wanna Try Again? (Y/N)\n".lower())
    if (choice == 'y'):
        print("Lets Go! Game makes mind refreshing!")
        counter += 1 
        if (secret_num <= 30 and secret_num >= 1): # Trying to give hints 
            print("I guess you should focus on numbers between 1 to 30 {^.'} ")
        elif (secret_num >= 30 and secret_num <= 50 ):
            print("I guess you should focus on numbers between 30 to 50 {^.'} ")
        elif (secret_num >= 50 and secret_num <= 70 ):
            print("I guess you should focus on numbers between 50 to 70 {^.'} ")
        elif (secret_num >= 70 and secret_num <= 100 ):
            print("I guess you should focus on numbers between 70 to 100 {^.'} ")
        else:
            print("Invalid input!")
        continue
    elif (choice == 'n'): 
        break
    else:
        print("Invalid input")
        break
    
print("--- You Got Tired! ---") 
print(f"Game Count: {counter}")
        

   
