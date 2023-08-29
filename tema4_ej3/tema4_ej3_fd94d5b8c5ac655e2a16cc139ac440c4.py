def jerigonzo(string):
    vowels = "aeiouAEIOU"
    jerigonzo_text = ""
    for char in string:
        jerigonzo_text += char
        if char in vowels:
            jerigonzo_text += "p" + char.lower()
    return jerigonzo_text

if __name__ == "__main__":
    text = input("Ingrese un texto: ")
    print(jerigonzo(text))

         