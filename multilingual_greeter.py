def greet_english(name):
    print('Hello',name)

def greet_spanish(name):
    print('Hola',name)

def greet_french(name):
    print('salut',name)

def name_input_english():
    name = input("What is your name?\n") 
    greet_english(name)

def name_input_spanish():
    name = input("cuál es tu nombre?\n") 
    greet_spanish(name)

def name_input_french():
    name = input("quel est ton nom?\n") 
    greet_french(name)

def language_input():
    type_of_language = input("English\nSpanish\nFrench\n")
    if type_of_language == "English":
        name_input_english()
    elif type_of_language == "Spanish":
        name_input_spanish()
    elif type_of_language == "French":
        name_input_french()
    else:
        print('error')
    

language_input()
