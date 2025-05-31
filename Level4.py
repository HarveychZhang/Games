import time as t

while True:
    print("Hello, welcome to Level4")
    t.sleep(1)
    print("Animal interesting questions Level 4 is in preparation")
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
    guess = input("1)What bird has no wings?\nA.Raphus Cucullatus\nB.Giant Moas\nC.Kiwi\nD.Casuarius\nEnter:")
    if guess == "C":
        print("Your answer is correct! +1point.")
        print("Analyze: Kiwis are the national bird of New Zealand and an icon of the country. Kiwis get their name from their shrill 'keee-weee' call. Because the kiwi has no wings, it cannot fly.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'C'.")
        print("Analyze: Kiwis are the national bird of New Zealand and an icon of the country. Kiwis get their name from their shrill 'keee-weee' call. Because the kiwi has no wings, it cannot fly.\n")

    t.sleep(5)
    guess = input("2)The animals with the highest protein content ever found are:\nA.Lobster\nB.Prawn\nC.Acetes\nD.Krill\nEnter:")
    if guess == "D":
        print("Your answer is correct! +1point.")
        print("Analyze: Krill is much higher in protein than beef or fish. A fresh krill, stripped of water, is almost entirely protein.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'D'.")
        print("Analyze: Krill is much higher in protein than beef or fish. A fresh krill, stripped of water, is almost entirely protein.\n")

    t.sleep(5)
    guess = input("3)Whether it is cold or heat, whether it is Rocky Mountains, rolling hills, dense forests, open plains, endless desert, there are traces everywhere. The animals that are so widely distributed are:\nA.Fox\nB.Tiger\nC.Wolf\nD.Bear\nEnter:")

    if guess == "C":
        print("Your answer is correct! +1point.")
        print("Analyze: Five million years before humans flourished, wolves were the most widespread on the planet. In Europe, Asia and America, where wolves are widely distributed, the records of wolves in North America alone have reached 23 species, and the number of subspecies is too numerous to enumerate.")
        t.sleep(5)
        print("------------------------------------------------------------------------")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'C'.")
        print("Analyze: Five million years before humans flourished, wolves were the most widespread on the planet. In Europe, Asia and America, where wolves are widely distributed, the records of wolves in North America alone have reached 23 species, and the number of subspecies is too numerous to enumerate.")
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
        import Level5
        break

    elif ask == "z":
        print("Quit to the menu...")
        import Introduction
        break