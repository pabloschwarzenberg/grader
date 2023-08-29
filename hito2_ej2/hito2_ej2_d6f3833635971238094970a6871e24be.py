def genoma(string):
    letras = ("A","T","C","G")
    string = string.upper()
    for i in string:
        if i not in letras:
            return False
    return True

string = input("Ingrese la secuencia: ")
if genoma(string)==False:
    print("secuencia incorrecta")
if genoma(string)==True:
    print("secuencia correcta")