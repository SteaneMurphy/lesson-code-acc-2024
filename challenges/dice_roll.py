import random

def roll(dice):
    roll_list = []
    amount_of_dice = int(dice[0])
    sides = int(dice[2:])
    for i in range(amount_of_dice):                 # for amount of dice
        roll_list.append(random.randint(1, sides))     # random number from 1 to amount of sides
    
    dice_dict = { "dice": roll_list }
    dice_dict["total"], dice_dict["highest"] = sum_rolls(roll_list)
    
    print(dice_dict)

def sum_rolls(rolls):
    result = 0
    highest = 0
    for i in rolls:
       if i > highest:
           highest = i
       result += i

    return result, highest 

roll('3d10')