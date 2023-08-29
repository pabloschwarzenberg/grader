def jerigonzo(string):
    palabra=[]
    for i in range(0,len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
            palabra.append(string[i])
            palabra.append("p")
            palabra.append(string[i])
        else:
            palabra.append(string[i])
    return "".join(palabra)