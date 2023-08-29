def jerigonzo(string):
    vocales = ["a","e","i","o","u","á","é","í","ó","ú"]
    stringF = ""
    for a in range(len(string)):
        if string[a] in vocales:
            stringF += string[a]+"p"+string[a]
        else:
            stringF += string[a]
    return stringF

if __name__ == "__main__":
    pass
         