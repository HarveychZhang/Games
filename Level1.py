import time as t

while True:
    print("Hello, welcome to Level1")
    t.sleep(1)
    print("Animal interesting questions Level 1 is in preparation")
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
    guess = input("1)What insects do frogs eat only?\nA.Insects that cling to aquatic plants\nB.Insects in the rice field\nC.Insects lying on the ground\nD.Insect in motion\nEnter:")
    if guess == "D":
        print("Your answer is correct! +1point.")
        print("Analyze: The eye of the frog is a pale screen, nothing is seen, but when the flying insect comes into its field of vision, the image of the insect appears on the pale screen.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'D'.")
        print("Analyze: The eye of the frog is a pale screen, nothing is seen, but when the flying insect comes into its field of vision, the image of the insect appears on the pale screen.\n")

    t.sleep(5)
    guess = input("2)Animals that use their tails to support their bodies is:\nA.Tiger\nB.Sapajou\nC.Kangaroo\nD.Fish\nEnter:")
    if guess == "C":
        print("Your answer is correct! +1point.")
        print("Analyze: Under normal circumstances, kangaroo forelimbs are not ground, often use hind limbs and tail support body.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'C'.")
        print("Analyze: Under normal circumstances, kangaroo forelimbs are not ground, often use hind limbs and tail support body.\n")

    t.sleep(5)
    guess = input("3)Where does the bat's echolocator come from, which is like a living radar?\nA.Abdomen\nB.Ear\nC.Throat\nD.Eye\nEnter:")

    if guess == "C":
        print("Your answer is correct! +1point.")
        print("Analyze: The bat's throat emits a very strong ultrasonic sound, which is emitted outward through its mouth and nose.")
        t.sleep(5)
        print("------------------------------------------------------------------------")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'C'.")
        print("Analyze: The bat's throat emits a very strong ultrasonic sound, which is emitted outward through its mouth and nose.")
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

    ask = input("Choose what you want:\nEnter n to quit the game, Enter y to Try again, Enter x to the next level, Enter z to quit to the menu.\nEnter:")

    if ask == "y":
        print("again")

    elif ask == "n":
        import End
        break

    elif ask == "x":
        print("Move to the next level...")
        print(".", end="")
        t.sleep(1)
        print(".", end="")
        t.sleep(1)
        print(".")
        t.sleep(1)
        print("\n\n\n")
        import Level2
        break

    elif ask == "z":
        print("Quit to the menu...")
        import Introduction
        break