def jerigonzo(string):
    vowels = "aeiouAEIOU"
    jerigonzo_text = ""
    for char in string:
        if char in vowels:
            jerigonzo_text += char + "p" + char.lower()
        else:
            jerigonzo_text += char
    return jerigonzo_text
