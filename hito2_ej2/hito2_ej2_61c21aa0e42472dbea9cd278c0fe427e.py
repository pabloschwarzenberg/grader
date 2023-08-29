def validar_secuencia(string):
    l = ["a", "c", "t", "g"]
    i = 0
    for letter in string:
        if letter not in l:
            i += 1
        else:
            i += 0
    if i == 0:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")

string = input()

validar_secuencia(string)      