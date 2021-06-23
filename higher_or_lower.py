import random

def user_number():
    number = input('Pick a number 0-10\n')
    return int(number)
    
def rand_number():
    number = random.randrange(0,11)
    return number
    
def compare_number():
    user = user_number()
    rand = rand_number()
    if user > rand:
        print('that was too high\nyour number was',user,
        '\nthe random number was',rand)
    elif user < rand:
        print('that was too low\nyour number was',user,
        '\nthe random number was',rand)
    elif user == rand:
        print('that was spot on\nyour number was',user,
        '\nthe random number was',rand)
    else:
        print('error')

compare_number()