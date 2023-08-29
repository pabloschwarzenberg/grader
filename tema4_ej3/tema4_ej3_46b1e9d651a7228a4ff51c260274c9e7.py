def jerigonzo(string):
    vowels = "aeiouáéíóú"
    translated_text = ""
    
    for char in string:
        if char.lower() in vowels:
            translated_text += char + "p" + char.lower()
        else:
            translated_text += char
    
    return translated_text

if __name__ == "__main__":
    text = input("Ingrese un texto: ")
    translated_text = jerigonzo(text)
    print("Texto original:", text)
    print("Texto traducido a jerigonzo:", translated_text)

         