def jerigonzo(string):
    vowels = "aeiou"
    translated = ""
    for char in string:
        translated += char
        if char.lower() in vowels:
            translated += "p" + char.lower()
    return translated

if __name__ == "__main__":
    text = input("Ingresa un texto: ")
    translated_text = jerigonzo(text)
    print("Texto traducido a jerigonzo:", translated_text)
