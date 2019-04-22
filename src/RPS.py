import random
#welcome message 

def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

# def save_results(w,t,l):
#     text_file = open("hisotry.text", "w")
#     text_file.write(str(w) + "," + str(t) + "," + str(l))
#     text_file.close()

results = load_results()
wins = int(results[0]) 
ties = int(results[1]) 
losses = int(results[2]) 

print("Welcome to RPS!")
print("Wins: %s, Ties %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")

computer = random.randint(1,3)
user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))

while not user == 9:
    if user == 1:
        if computer == 1:
            print("Computer chose rock... tie!")
            ties +=1
        elif computer == 2:
            print("Computer chose paper... computer wins :(")
            losses += 1
        else:
            print("Computer chose scissors... you wins :)")
            wins+=1
    elif user == 2:
        if computer == 1:
            print("Computer chose rock... you wins :)")
            wins +=1
        elif computer == 2:
            print("Computer chose paper... tie!")
            ties += 1
        else:
            print("Computer chose scissors... computer wins :(")
            losses+=1
    elif user == 3:
        if computer == 1:
            print("Computer chose rock... computer wins :(")
            losses +=1
        elif computer == 2:
            print("Computer chose paper... you wins :)!")
            wins += 1
        else:
            print("Computer chose scissors... tie!")
            ties+=1 
    else:
        print("Invalid selection. Please try again")
    
save_results(wins, ties, losses)
print("Wins: %s, Ties %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")

    computer = random.randint(1,3)
    # user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n")