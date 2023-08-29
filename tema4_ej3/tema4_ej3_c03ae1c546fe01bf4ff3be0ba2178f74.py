def jerigonzo(string):
    string = list(string)
    for i in range(0,len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
            string[i] += "p"
            string[i] += string[i]
            string[i] = list(string[i])
            del string[i][-1]
            string[i] = "".join(string[i])
    return "".join(string)