def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    for vocal in vocales:
        if vocal in string:
            print(vocal)
            string=string.replace(vocal,vocal+"p"+vocal)
    return string

if __name__ == "__main__":
    pass
         