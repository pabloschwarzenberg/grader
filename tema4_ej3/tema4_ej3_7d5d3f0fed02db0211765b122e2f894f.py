def jerigonzo(string):   
    for x in string:
        voc = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i = 0
    while i < len(voc):
        a = voc[i] + "p" + voc[i] 
        string = string.replace(voc[i], a)
        i += 1
    return string