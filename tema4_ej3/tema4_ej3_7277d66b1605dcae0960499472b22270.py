def jerigonzo(text):
    new_text = ""
    for letter in text:
        if letter in "aeiouAEIOU":
            new_text += letter + 'p' + letter
        else:
            new_text += letter
    return new_text

if __name__ == "__main__":
    print("Jerigonzo:", jerigonzo(input("Texto: ")))
