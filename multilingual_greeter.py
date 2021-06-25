def greet(name):
    '''takes name and greet user with given name'''
    print ("Hola " + name)
    

def name_input():
    '''Promts user for input and returns string'''
    x=input("What do you like people to call you?")
    return x  

lang = input("Morning what is your first language english, spanish or italian?:")
while(lang != 'english') and (lang != 'spanish') and (lang != 'italian'):
    lang = input("Morning what is you first language ")


    


    
z = name_input()
greet(z)