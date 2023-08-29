def jerigonzo(string):

    string2 = ""
    vMin = ["a","e","i","o","u"]
    vMay = ["A","E","I","O","U"]
    val = False
    for i in range(len(string)):
        for j in range(len(vMay)):
            if string[i]==vMin[j] or string[i] == vMay[j]:
                vocal = string[i]
                string2+=string[i]
                string2+="p"
        string2+=string[i]

    return string2
         