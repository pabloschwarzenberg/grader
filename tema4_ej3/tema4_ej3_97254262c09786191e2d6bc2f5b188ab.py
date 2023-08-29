def jerigonzo(string):
    vowels = "aeiouAEIOU"
    translated_text = ""
    for char in string:
        if char in vowels:
            translated_text += char + "p" + char.lower()
        else:
            translated_text += char
    return translated_text

if __name__ == "__main__":
    text = input("Ingresa un texto: ")
    translated_text = jerigonzo(text)
    print("Texto traducido a jerigonzo:", translated_text)
