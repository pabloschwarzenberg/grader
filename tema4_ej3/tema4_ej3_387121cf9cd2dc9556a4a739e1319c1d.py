def jerigonzo(string):
    translated = ""
    vowels = "aeiouAEIOU"
    
    for char in string:
        translated += char
        if char in vowels:
            translated += "p" + char.lower()
    
    return translated


if __name__ == "__main__":
    text = input("Ingrese un texto: ")
    translated_text = jerigonzo(text)
    print("Texto traducido al jerigonzo:", translated_text)
