def main():
    print("Welcome to the Adventure of Link!")
    print("You wake up in a mysterious forest. The Triforce glows faintly in your hand.")
    print("You see a path leading deeper into the woods and another path leading to a riverbank. Which way do you go?")
    
    path = input("1. Follow the forest path\n2. Head towards the riverbank\n> ")
    
    if path == "1":
        print("You follow the forest path and come across a clearing with a strange old man.")
        print("He offers you a sword and shield. Do you accept?")
        
        choice = input("1. Accept the sword and shield\n2. Decline and continue on\n> ")
        
        if choice == "1":
            print("You accept the sword and shield and feel a surge of power.")
            print("The old man points you towards a cave. Do you enter?")
            
            cave = input("1. Enter the cave\n2. Ignore the cave and explore the forest\n> ")
            
            if cave == "1":
                print("You enter the cave and find a treasure chest.")
                print("Inside the chest, you find the Master Sword!")
                print("You are now ready to face the challenges ahead. Well done, hero!")
            elif cave == "2":
                print("You explore the forest further and find a hidden fairy fountain.")
                print("The fairy heals your wounds and grants you a special ability.")
                print("Feeling rejuvenated, you continue your journey.")
            else:
                print("You stand there indecisively and are ambushed by monsters. Game over!")
        elif choice == "2":
            print("You decline the offer and continue on.")
            print("As you walk, you stumble upon a hidden entrance to a dungeon.")
            print("Do you dare to explore the dungeon?")

            dungeon = input("1. Enter the dungeon\n2. Ignore the dungeon and keep walking\n> ")

            if dungeon == "1":
                print("You enter the dungeon and encounter puzzles and monsters.")
                print("After a long and challenging journey, you find a piece of the Triforce!")
                print("You are one step closer to saving Hyrule. Keep going!")
            elif dungeon == "2":
                print("You decide to ignore the dungeon and keep walking.")
                print("You come across a friendly merchant who offers to sell you rare items.")
                print("You purchase some useful supplies and continue your adventure.")
            else:
                print("You hesitate too long and are captured by wandering monsters. Game over!")
        else:
            print("You stand there unsure and a monster attacks you. Game over!")
    
    elif path == "2":
        print("You head towards the riverbank and find a boat.")
        print("Do you get in the boat and sail down the river?")
        
        boat = input("1. Get in the boat\n2. Explore the riverbank\n> ")
        
        if boat == "1":
            print("You sail down the river and discover a hidden waterfall.")
            print("Behind the waterfall, you find a secret entrance to a dungeon.")
            print("Do you dare to enter the dungeon?")

            dungeon = input("1. Enter the dungeon\n2. Return to the forest\n> ")

            if dungeon == "1":
                print("You enter the dungeon and face many challenges.")
                print("Deep within, you find a magical artifact that grants you new powers.")
                print("You are now stronger than ever. Onward, hero!")
            elif dungeon == "2":
                print("You decide to return to the forest.")
                print("As you walk, you stumble upon a hidden fairy fountain.")
                print("The fairy heals your wounds and grants you a special ability.")
                print("Feeling rejuvenated, you continue your journey.")
            else:
                print("You hesitate too long and the boat drifts into dangerous waters. Game over!")
        elif boat == "2":
            print("You explore the riverbank and find a hidden cave.")
            print("Inside the cave, you find a treasure chest.")
            print("Do you open the chest?")

            chest = input("1. Open the chest\n2. Leave the chest and continue exploring\n> ")

            if chest == "1":
                print("You open the chest and find a powerful magic item.")
                print("With this item, you feel unstoppable. Onward, hero!")
            elif chest == "2":
                print("You decide to leave the chest and continue exploring.")
                print("You come across a friendly merchant who offers to sell you rare items.")
                print("You purchase some useful supplies and continue your adventure.")
            else:
                print("You stand there indecisively and are ambushed by monsters. Game over!")
        else:
            print("You stand there unsure and a monster attacks you. Game over!")
    
    else:
        print("You're too indecisive and get lost in the woods. Game over!")

if __name__ == "__main__":
    main()
