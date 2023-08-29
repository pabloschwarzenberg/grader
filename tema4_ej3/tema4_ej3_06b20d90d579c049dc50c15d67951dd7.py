def jerigonzo(string):
    string1 = []
    string2 = ""
    for i in string:
       string1.append(i)
       if i == "a":
         pa = "pa"
         string1.append(pa)
       elif i == "e":
         pe = "pe"
         string1.append(pe)
       elif i == "i":
         pi = "pi"
         string1.append(pi)
       elif i == "o":
         po = "po"
         string1.append(po)
       elif i == "u":
         pu = "pu"
         string1.append(pu)

    for j in string1:
        string2 = string2 + str(j)
       
    return string2

