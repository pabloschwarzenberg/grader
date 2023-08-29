def jerigonzo(string):
    nuevoString = ''
    for letter in string:
        if letter in 'aeiou':
            nuevoString += letter+'p'+letter
        else:
            nuevoString += letter
    string = nuevoString
    return string

if __name__ == "__main__":
    string = input()
    jerigonzo(string)
         