def jerigonzo(string):
    jer = ""
    for i in string:
        jer += i
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            jer += "p"
            jer += i
    return jer