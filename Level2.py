import time as t

while True:
    print("Hello, welcome to Level2")
    t.sleep(1)
    print("Animal interesting questions Level 2 is in preparation")
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
    guess = input("1)How many times a cat's eyes change every day?\nA.1 time\nB.2 times\nC.3 times\nD.4 times\nEnter:")
    if guess == "C":
        print("Your answer is correct! +1point.")
        print("Analyze: Morning like a date stone, noon into a line, like the full moon at night. The cat has a large pupil and a strong sphincter, which adjusts the pupil to the light in different conditions.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'C'.")
        print("Analyze: Morning like a date stone, noon into a line, like the full moon at night. The cat has a large pupil and a strong sphincter, which adjusts the pupil to the light in different conditions.\n")

    t.sleep(5)
    guess = input("2)What's the result of casting pearls before swine?\nA.The cow estrus\nB.Cows yield much milk\nC.The bull angry\nD.The cattle dance\nEnter:")
    if guess == "B":
        print("Your answer is correct! +1point.")
        print("Analyze: Cows have hearing and an intact nervous system, and music can encourage them to produce more milk.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'B'.")
        print("Analyze: Cows have hearing and an intact nervous system, and music can encourage them to produce more milk.\n")

    t.sleep(5)
    guess = input("3)Animals that give birth only to 'daughters' but not 'cubs' are: \nA.Loach\nB.Tortoise\nC.Terrapin\nD.Ricefield eel\nEnter:")

    if guess == "D":
        print("Your answer is correct! +1point.")
        print("Analyze: From the egg hatched out of the small eel, only the ovaries, are female, grow up the internal changes of the ovary, the ovaries become testis, eel also from the female into male. Biologists call this a 'sex reversal.'")
        t.sleep(5)
        print("------------------------------------------------------------------------")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'D'.")
        print("Analyze: From the egg hatched out of the small eel, only the ovaries, are female, grow up the internal changes of the ovary, the ovaries become testis, eel also from the female into male. Biologists call this a 'sex reversal.'")
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
        import Level3
        break

    elif ask == "z":
        print("Quit to the menu...")
        import Introduction
        break