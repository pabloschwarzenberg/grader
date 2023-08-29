def jerigonzo(string):
    p= "p"
    oracionA=""
    for i in (string):
        if (i == "a" or i== "e" or i== "i" or i== "o" or i== "u"):
            oracionA=oracionA + i + p + i
        elif (i != "a" or "e" or "i" or "o" or "u"):
            oracionA=oracionA+i
    return oracionA

if __name__ == "__main__":
    pass
         