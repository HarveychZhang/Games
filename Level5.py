import time as t

while True:
    print("Hello, welcome to Level5")
    t.sleep(1)
    print("Animal interesting questions Level 5 is in preparation")
    t.sleep(1)
    print(".", end="")
    t.sleep(1)
    print(".", end="")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print("Now let's do the animal fun questions!")
    t.sleep(2)
    total = 0
    guess = input("1)It takes only 0.05 seconds for the mantis to capture the insect from the pouncing to the whole process, and it hits the target every time. This mainly depends on:\nA.Protective Body Color\nB.Tracking and Aiming System for Compound Eyes\nC.Sharp Forefeet\nD.Special Body Type with Low Air Resistance\nEnter:")
    if guess == "B":
        print("Your answer is correct! +1point.")
        print("Analyze: The tracking and aiming system of mantis compound eye can quickly measure the coming and going direction, speed and distance of small insects flying in front of them.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'B'.")
        print("Analyze: The tracking and aiming system of mantis compound eye can quickly measure the coming and going direction, speed and distance of small insects flying in front of them.\n")

    t.sleep(5)
    guess = input("2)Animals that drool a lot are:\nA.Cattle\nB.Cat\nC.Dog\nD.Rabbit\nEnter:")
    if guess == "A":
        print("Your answer is correct! +1point.")
        print("Analyze: Cattle have no digestive secretions in their stomachs, so food cannot be digested directly. Cattle produce large amounts of saliva to aid digestion after chewing the cud.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'A'.")
        print("Analyze: Cattle have no digestive secretions in their stomachs, so food cannot be digested directly. Cattle produce large amounts of saliva to aid digestion after chewing the cud.\n")

    t.sleep(5)
    guess = input("3)Why do monkeys eat so fast?\nA.Chewing fast\nB.Hungry\nC.Good digestion\nD.There are 'pockets' on both sides of the mouth\nEnter:")

    if guess == "D":
        print("Your answer is correct! +1point.")
        print("Analyze: Monkeys have pouches on each side of their mouths, called cheek pouches, which they use for food storage. They store their food in cheek pouches and chew it slowly afterwards, which seems to make them eat more quickly.")
        t.sleep(5)
        print("------------------------------------------------------------------------")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'D'.")
        print("Analyze: Monkeys have pouches on each side of their mouths, called cheek pouches, which they use for food storage. They store their food in cheek pouches and chew it slowly afterwards, which seems to make them eat more quickly.")
        t.sleep(5)
        print("------------------------------------------------------------------------")

    t.sleep(2)
    print("Your score is being calculated")
    t.sleep(1)
    print(".", end="")
    t.sleep(1)
    print(".", end="")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print("Finish")
    t.sleep(1)
    print("Your total point is:", total)
    t.sleep(2)

    print("Congratulations, you've completed the Animal Fun question with 15 questions in 5 levels, Bravo!!!")
    t.sleep(3)

    ask = input("Choose what you want:\nEnter n to quit the game, Enter y to Try again, Enter z to quit to the menu.\nEnter:")

    if ask == "y":
        print("again")

    elif ask == "n":
        import End
        break

    elif ask == "z":
        print("Quit to the menu...")
        import Introduction
        break