def jerigonzo(string):
    jerigonzo_text = ""
    vowels = "aeiouAEIOU"
    
    for char in string:
        jerigonzo_text += char
        if char in vowels:
            jerigonzo_text += "p" + char
    
    return jerigonzo_text

if __name__ == "__main__":
    text = input("Ingresa un texto: ")
    translated_text = jerigonzo(text)
    print("Texto traducido al jerigonzo:", translated_text)
         