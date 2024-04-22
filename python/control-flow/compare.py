name = input('name: ')

match name:
    case 'hermione' | 'harry' | 'ron':
        print('gryffindor')
    case 'draco':
        print('slytherin')
    case _:
        print('error')
