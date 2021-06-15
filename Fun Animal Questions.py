import random
import time as t

while True:
    print("Animal interesting questions and answers are in preparation")
    t.sleep(1)
    print(".",end="")
    t.sleep(1)
    print(".",end="")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print("Now let's do the animal fun questions!")
    t.sleep(2)
    print("When you answer the question, press the 'Enter'")
    t.sleep(2)
    total = 0
    q = input("1)What is the biggest animal in the sea at present?\nA.Humpback\nB.Killer Whale\nC.Tiger Shark\nD.Blue Whale")
    guess = input("Enter: ")
    if guess == "D":
        print("Your answer is correct! +1point.")
        total = total + 1
    else:
        print("Your answer is wrong! No point.")
        
    t.sleep(3)
    q = input("2)What is the biggest animal in the land at present?\nA.Rabit\nB.Rhino\nC.Elephant\nD.Giraffe")
    guess = input("Enter: ")
    if guess == "C":
        print("Your answer is correct! +1point.")
        total = total + 1
    else:
        print("Your answer is wrong! No point.")
    
    t.sleep(3)
    q = input("3)What is the smartest animal in the world\nA.Gorilla\nB.Killer Whale\nC.Dolphin\nD.Baboon")
    guess = input("Enter: ")
            
    if guess == "A":
        print("Your answer is correct! +1point.\n------------------------------------------------------------------------")
        total = total + 1
    else:
        print("Your answer is wrong! No point.\n------------------------------------------------------------------------")
    
    t.sleep(2)
    print("Your score is being calculated")
    t.sleep(1)
    print(".",end="")
    t.sleep(1)
    print(".",end="")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print("Finish")
    t.sleep(1)
    print("Your total point is:", total)
    t.sleep(2)
                
    ask = input("Do you want to try again or quit?\nEnter n to quit, Enter y to Try again...\nEnter:")
    
    if ask == "y":
        print("again")
    
    elif ask == "n":
        print("The question ends...")
        break