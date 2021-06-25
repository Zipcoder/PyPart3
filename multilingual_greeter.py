def greet(name):
    ''' prints a greeting to the name variable .'''
    print('hello ' + name)

greet('Sean')
greet('Darth Vader')
greet("Guido van Rossum")

def name_input():
    ''' Asks user for their name and then returns said name. '''
    name = input('Please enter your name\n')
    return name


greet(name_input())

def language_input():
    user = name_input()
    chosen_language = input("Please select English, French, or Spanish\n")
    if chosen_language.lower() == 'english':
        return 'Hello ' + user
    elif chosen_language.lower() == 'french':
        return 'Bonjour ' + user
    elif chosen_language.lower() == 'spanish':
        return 'Hola ' + user
print(language_input())