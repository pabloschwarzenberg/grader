abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def special(a):
    if a < 13:
        a = a+13
    else:
        a = a-13
    return a

def rot13(palabra):
    global abc
    codif = []
    codifpalabra = ""
    palabralist = list(palabra)
    for i in range(0,len(palabra)):
        j = palabralist[i]
        cont=0
        while abc[cont]!=j and cont<30:
            cont = cont+1
        if cont < 30:
            codif.append(abc[special(cont)])
        else:
            codif.append(j)
    for i in range(0,len(palabra)):
        codifpalabra = codifpalabra+str(codif[i])
    return codifpalabra


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           