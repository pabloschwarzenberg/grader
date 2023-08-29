def rot13(palabra):
    abecedario= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lista=[]
    for x in palabra:
        for y in abecedario:
            if x==y:
                for z in range(len(abecedario)):
                    if abecedario[z] == y:
                        a=z+13
                        if a>=26:
                            b=26-z
                            a=13-b
                        lista.append(abecedario[a])
    
    palabra= ''.join(lista)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           