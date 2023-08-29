def jerigonzo(string):
    x = ""
    for i in string:
        
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            x = x + i + "p" + i
        else:
            x = x + i
    string = x
    return string


         