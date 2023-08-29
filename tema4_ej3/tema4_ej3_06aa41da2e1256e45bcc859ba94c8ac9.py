def jerigonzo(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    translated_text = ''
    for char in string:
        translated_text += char
        if char.lower() in vowels:
            translated_text += 'p' + char.lower()
    return translated_text

if __name__ == "__main__":
    text = input("Ingrese un texto: ")
    translated_text = jerigonzo(text)
    print("Texto traducido al jerigonzo:", translated_text)
