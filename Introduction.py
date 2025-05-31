import time as t
import emoji

print("Welcome to Fun Animal Question. In here, you will learn a lot about animals.")
t.sleep(1)
print(emoji.emojize(":cat: :dog: :mouse: :hamster: :rabbit: :wolf: :frog: :tiger: :koala: :bear: :pig: :cow: :boar: :monkey: :horse: :camel: :sheep: :elephant: :panda_face: :snake: :bird: :chicken: :penguin: :turtle: :bug: :honeybee: :ant: :beetle: :snail: :octopus: :tropical_fish: :fish: :whale: :whale2: :dolphin: :cow2: :ram: :rat: :water_buffalo: :tiger2: :rabbit2: :dragon: :goat: :rooster: :dog2: :pig2: :mouse2: :ox: :dragon_face: :blowfish: :crocodile: :dromedary_camel: :leopard: :cat2: :poodle:", use_aliases=True))
t.sleep(3)
print("You just have to answer them to the best of your ability.")
t.sleep(3)
print("Don't worry if you get it wrong, it's just a game.\n")
t.sleep(3)
Level = input("Please enter the level you want to play, a total of 5 levels.\nIf you want to warm up, type 'Practice'.\nOr if you wanna quit the game, Please enter 'Quit'\nEnter:")
if Level == "1":
    import Level1
if Level == "2":
    import Level2
if Level == "3":
    import Level3
if Level == "4":
    import Level4
if Level == "5":
     import Level5
if Level == "Quit the game":
    import End
elif Level == "Practice":
    import Practice