import random


health = 100
gold = 10
game_active = True


def explore():
    print("You are exploring...")
    encounter = random.choice(["monster", "gold", "rest", "nothing"])

    if encounter == "monster":
        print("A wild monster appears! ")
        fight_monster()
    elif encounter == "gold":
        found_gold = random.randint(10,50)
        print(f"You found some {found_gold} gold! ")
        global gold
        gold += found_gold
    elif encounter == "rest":
        print("I feel tried, I will rest for now")
        rest()
    else:
        print("You found nothing")


def fight_monster():
    global health
    monster_damage = random.randint(10,45)
    print(f"The monster attacks you and deals {monster_damage} damage! ")
    health -= monster_damage
    if health > 0:
        print(f"Your health is {health}")
    else:
        print("You are dead!")

def rest():
    global health
    recovered_health = random.randint(10,25)
    health -= recovered_health
    if health > 100:
        health = 100
    print(f"You rested and got back {recovered_health} health. You health is {health}.")

while game_active and health > 0:
    print(f"\nCurrent Status: Health = {health}, gold = {gold}")
    action = input("Do you want to [explore] or [quit]?] ")

    if action == "explore":
        explore()
    elif action == "quit":
        game_active = False
        print("Thanks for playing!")
    else:
        print("Invalid input, enter 'explore' or 'quit'")

if health <= 0:
    print("You are dead!, Game over.")


