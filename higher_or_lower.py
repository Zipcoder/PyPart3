from random import randrange

def user_value():
    value = input('Please enter a number between 0 and 10\n')
    return value

def randomValue():
    return randrange(1, 10)

def isEqual():

    a = randomValue()
    b = user_value()
    b = int(b)

    print("Random # generated: " + str(a))

    print("you guessed: " + str(b))

    if a == b:
        print('You guessed correctly!')
    elif a > b:
        print('You guessed too low')
    else:
        print('You guessed too high!')

isEqual()