def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def jerigonzo(string):
    vocales = ["a", "e", "i", "o", "u"]
    agrega = ["apa", "epe", "ipi", "opo", "upu"]
    string1=""
    if vocales[0] in string:
        string = string.replace(vocales[0], agrega[0])
    if vocales[1] in string:
        string = string.replace(vocales[1], agrega[1])
    if vocales[2] in string:
        string = string.replace(vocales[2], agrega[2])
    if vocales[3] in string:
        string = string.replace(vocales[3], agrega[3])
    if vocales[4] in string:
        string = string.replace(vocales[4], agrega[4])
    return string