value = input("please provide a number between 0,10:\n")
    
value = int(value)
print(f'you entered {value}')

import random
a = random.randint(1,10)
print(a)

while a != value:
    print 
    if value < a:
        print ("guess is too low")
        break
    elif value > a: 
        print ("guess is too high")
        break
    else:
        print ("you guessed it")
        break
        
    


 
    
