import time as t

while True:
    print("Animal interesting questions Practice is in preparation")
    t.sleep(1)
    print(".", end="")
    t.sleep(1)
    print(".", end="")
    t.sleep(1)
    print(".")
    t.sleep(1)
    print("This is just practice, no parsing, because the questions are so easy.")
    t.sleep(2)
    print("Now let's practice!")
    t.sleep(2)
    guess = input("1)What is the biggest animal in the sea at present?\nA.Humpback\nB.Killer Whale\nC.Tiger Shark\nD.Blue Whale\nEnter:")
    if guess == "D":
        print("Your answer is correct!\n")
    else:
        print("Your answer is wrong! The correct answer is 'D'.\n")

    t.sleep(3)
    guess = input("2)What is the biggest animal in the land at present?\nA.Rabit\nB.Rhino\nC.Elephant\nD.Giraffe\nEnter:")
    if guess == "C":
        print("Your answer is correct!\n")
    else:
        print("Your answer is wrong! The correct answer is 'C'.\n")

    t.sleep(3)
    guess = input("3)What is the smartest animal in the world\nA.Gorilla\nB.Finback\nC.Dolphin\nD.Baboon\nEnter:")

    if guess == "A":
        print("Your answer is correct!\n------------------------------------------------------------------------")
    else:
        print("Your answer is wrong! The correct answer is 'A'.\n------------------------------------------------------------------------")

    print("Okay, so that's all the practice for the game. Then, here we go")

    ask = input("Choose what you want:\nEnter n to quit the game, Enter y to Try again, Enter x to the level 1, Enter z to quit to the menu.\nEnter:")

    if ask == "y":
        print("again")

    elif ask == "n":
        import End
        break

    elif ask == "x":
        print("Move to the level 1...")
        print(".", end="")
        t.sleep(1)
        print(".", end="")
        t.sleep(1)
        print(".")
        t.sleep(1)
        print("\n\n\n")
        import Level1
        break

    elif ask == "z":
        print("Quit to the menu...")
        import Introduction
        break