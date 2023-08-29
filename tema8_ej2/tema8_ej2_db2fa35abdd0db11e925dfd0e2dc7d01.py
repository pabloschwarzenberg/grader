def buscarTodas(a,b):
    string=""
    a2=list(a)
    for i in a2:
        if i==b:
            string=string + str(a2.index(i)) + " "
            a2[a2.index(i)]="_"
        else:
            continue   
    string.strip()
    return string


c=str(input("Introducir una frase o palabra: "))
d=str(input("Introducir una letra: "))
print(buscarTodas(c,d))