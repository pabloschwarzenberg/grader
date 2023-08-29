def jerigonzo(string):
    vocal="aeiouAEIOU"
    codificado = ""
    for A in string:
        if A in vocal:
            codificado += A
            codificado +="p"
        codificado += A


    return codificado