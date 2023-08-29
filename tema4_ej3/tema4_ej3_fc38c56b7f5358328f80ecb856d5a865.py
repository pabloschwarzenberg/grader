def jerigonzo(string):
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    for vocal in vocales:
        string=string.replace(vocal,vocal+"p"+vocal.lower())
    return string



if __name__ == "__main__":
    pass
         