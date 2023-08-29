def jerigonzo(string):
    translation = ""
    vowels = "aeiouAEIOU"

    for char in string:
        translation += char
        if char in vowels:
            translation += "p" + char

    return translation


if __name__ == "__main__":
    text = input("Ingresa un texto: ")
    translated_text = jerigonzo(text)
    print("Texto traducido a jerigonzo:", translated_text)
