def jerigonzo(string):
    vocales = "aeiouAEIOU"
    palabra = ""

    for n in range(len(string)):
        if vocales.count(string[n])>0:
            palabra += string[n] + "p"+ string[n]
        else:
            palabra += string[n]


    return palabra

if __name__ == "__main__":
    pass
         