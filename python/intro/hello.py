def card_validation(input):
    card_num = str(input)

    match card_num[0]:
        case "4":
            type = "visa"
        case "5":
            type = "mastercard"
        case _:
            print('\nSorry! We only accept Visa or Mastercard')
            return
        
    card_length = len(card_num)

    if card_length == 13 or card_length == 16:
        print('\nCard Number: Valid')
        print(f'Card Type: {type}')
        print(f'Bank: {card_num[1:6]}')
        print(f'Account: {card_num[6:card_length-1]}')
        print(f'Check Digit: {card_num[card_length-1:]}')
    else:
        print('\nThis card does not seem to be valid')

# valid Visa
card_validation(4988438843884305)
# valid Mastercard
card_validation(5555444433331111)
# Diner's Club - not accepted
card_validation(36006666333344)
# invalid input
card_validation('dsfgghfgfdsad')
# invalid input
card_validation(400000000000000)