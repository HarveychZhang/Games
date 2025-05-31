import time as t

while True:
    print("Hello, welcome to Level3")
    t.sleep(1)
    print("Animal interesting questions Level 3 is in preparation")
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
    guess = input("1)What is the world's most venomous jellyfish?\nA.Cyanea Capillata\nB.Cubozoa\nC.Irukandji Jellyfish\nD.Pelagia Noctiluca\nEnter:")
    if guess == "B":
        print("Your answer is correct! +1point.")
        print("Analyze: Cubozoa is a tiny jellyfish that lives mainly in the waters off the northeast coast of Australia and is believed to be the most toxic creature known to humans. It has gone mad to inject the most potent neurotoxin known to anyone who dares to mess with it. Stings are said to kill within 30 seconds of being stung.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'B'.")
        print("Analyze: Cubozoa is a tiny jellyfish that lives mainly in the waters off the northeast coast of Australia and is believed to be the most toxic creature known to humans. It has gone mad to inject the most potent neurotoxin known to anyone who dares to mess with it. Stings are said to kill within 30 seconds of being stung.\n")

    t.sleep(5)
    guess = input("2)What is the largest group of animals in the world?\nA.Krill Group\nB.Caribou Group\nC.Bee Group\nD.Dolphin Group\nEnter:")
    if guess == "A":
        print("Your answer is correct! +1point.")
        print("Analyze: Sometimes a swarm can form 500 meters long and hundreds of meters wide, and there can be as many as 30,000 krill per cubic meter of water.\n")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'A'.")
        print("Analyze: Sometimes a swarm can form 500 meters long and hundreds of meters wide, and there can be as many as 30,000 krill per cubic meter of water.\n")

    t.sleep(5)
    guess = input("3)What is an animal that can breathe through its intestines?\nA.Pufferfish\nB.Earthworm\nC.Sea Horse\nD.Loach\nEnter:")

    if guess == "D":
        print("Your answer is correct! +1point.")
        print("Analyze: The intestines of the loach connect the esophagus with the anus to form a straight tube, which is as thin and transparent as the casing. It is full of capillaries, thin and long, which can both digest the digestive function and breathe instead of the gills.")
        t.sleep(5)
        print("------------------------------------------------------------------------")
        total = total + 1
    else:
        print("Your answer is wrong! No point. The correct answer is 'D'.")
        print("Analyze: The intestines of the loach connect the esophagus with the anus to form a straight tube, which is as thin and transparent as the casing. It is full of capillaries, thin and long, which can both digest the digestive function and breathe instead of the gills.")
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
        import Level4
        break

    elif ask == "z":
        print("Quit to the menu...")
        import Introduction
        break