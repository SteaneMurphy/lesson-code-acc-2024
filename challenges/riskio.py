import random

def calculate_battle(*dice):
    attacker, defender = dice
    turns = len(attacker) if len(defender) > len(attacker) else len(defender)
    for i in range(turns):
        print(f'{compare_dice(attacker[i], defender[i])} loses an army')

def generate_dice():
    dice = []
    for i in range(random.randrange(1, 4)):
        dice.append(random.randrange(1,7))
    return dice

def compare_dice(a, d):
    if a > d:
        return "DEF"
    else:
        return "ATT"

calculate_battle(generate_dice(), generate_dice())