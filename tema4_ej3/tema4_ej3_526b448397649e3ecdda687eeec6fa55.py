def jerigonzo(string):
    jeri=""
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            jeri+=i
            jeri+="p"
        jeri+=i

    return jeri