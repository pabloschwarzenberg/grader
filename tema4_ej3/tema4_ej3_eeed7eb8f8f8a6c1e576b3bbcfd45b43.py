def jerigonzo(string):

    var_Vocales = ["a", "e", "i", "o", "u"]
    var_Texto = str()

    for var_Indice in string:
        if var_Indice in var_Vocales:
            var_Texto += (var_Indice + "p" + var_Indice)
        else:
            var_Texto += var_Indice

    return var_Texto

if __name__ == "__main__":
    pass