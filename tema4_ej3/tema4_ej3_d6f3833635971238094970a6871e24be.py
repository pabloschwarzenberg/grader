def jerigonzo(string):
    if "a" in string:
        string = string.replace("a","a"+"p"+"a")
    if "e" in string:
        string = string.replace("e","e"+"p"+"e")
    if "i" in string:
        string = string.replace("i","i"+"p"+"i")
    if "o" in string:
        string = string.replace("o","o"+"p"+"o")
    if "u" in string:
        string = string.replace("u","u"+"p"+"u")
    if "A" in string:
        string = string.replace("A","A"+"p"+"A")
    if "E" in string:
        string = string.replace("E","E"+"p"+"E")
    if "I" in string:
        string = string.replace("I","I"+"p"+"I")
    if "O" in string:
        string = string.replace("O","O"+"p"+"O")
    if "U" in string:
        string = string.replace("U","U"+"p"+"U")
    return string

if __name__ == "__main__":
    pass
         