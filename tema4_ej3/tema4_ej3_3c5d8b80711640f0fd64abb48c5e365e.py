    
def jerigonzo(string):
    vowels = "aeiouAEIOU"
    jerigonzo_string = ""
    for letter in string:
        if letter in vowels:
            jerigonzo_string += letter + "p" + letter.lower()
        else:
            jerigonzo_string += letter
    return jerigonzo_string

if __name__ == "__main__":
    print(jerigonzo("Hola mundo"))

         