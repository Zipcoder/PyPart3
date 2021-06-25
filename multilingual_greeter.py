
def name_input(lang):
    '''Promts user for input and returns string'''
    name = ""
    if lang == "english":
        name = input("what is you name")
    elif lang == "spanish":
        name = input("como te llamas")
    else: 
       name = input("come si chiama")
    return name 

def get_language():
    """asks user to choose one of three languages"""
    a = input("whats you first language? english, spanish, or french?")
    return a 


def greet_user(lang, name):
    '''Takes in the language and greets the user in that language'''
    if lang == "english":
        print("hello", name)
    elif lang == "spanish":
        print("hola", name)
    else: 
       print("ciao", name)


def main():
    language = get_language()
    name = name_input(language)
    greet_user(language, name)


if __name__ == "__main__":
    main() 