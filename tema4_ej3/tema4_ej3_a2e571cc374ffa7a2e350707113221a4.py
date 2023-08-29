def jerigonzo(string):
    contlet = 0
    string_list = []
    contj = 0
    n = 0
    lenstr = len(string)
    vocales = ["a", "e", "i", "o", "u"]
    while contlet < len(string):
        string_list.append(string[contlet])
        contlet += 1
    while contj < lenstr:
        letra = string_list[contj]
        cero_o_uno = vocales.count(letra)
        if cero_o_uno == 1:
            string_list.insert(contj+1, "p"+letra)
            contj += 1
            lenstr += 1
        contj += 1
    string = "".join(str(x) for x in string_list)
    return string
if __name__ == "__main__":
    pass
         