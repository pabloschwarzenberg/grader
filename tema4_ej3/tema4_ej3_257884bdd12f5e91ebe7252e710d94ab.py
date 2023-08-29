def jerigonzo(string):
    string_uno = []
    string_dos = ""
    for i in string:
       string_uno.append(i)
       if i == "a":
         pa = "pa"
         string_uno.append(pa)
       elif i == "e":
         pe = "pe"
         string_uno.append(pe)
       elif i == "i":
         pi = "pi"
         string_uno.append(pi)
       elif i == "o":
         po = "po"
         string_uno.append(po)
       elif i == "u":
         pu = "pu"
         string_uno.append(pu)

    for j in string_uno:
        string_dos = string_dos + str(j)

    return string_dos