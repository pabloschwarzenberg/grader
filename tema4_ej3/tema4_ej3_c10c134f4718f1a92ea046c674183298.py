def jerigonzo(string):
    vocales = "A,a,E,e,I,i,O,o,U,u,"
    palabra = ""
    for i in string:
        if i in vocales:
            palabra += i
            palabra += "p"
        palabra += i
    return palabra 
if __name__ == "__main__":
    pass
         