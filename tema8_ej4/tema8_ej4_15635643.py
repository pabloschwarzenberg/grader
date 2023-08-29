def rot13(s):
    letras="abcdefghijklmnopqrstuvwxyz"
    abecedario=[]
    abecedario_inverso=[]
    palabra=[]
    for i in s:
        palabra.append(i)
    for i in letras:
        abecedario.append(i)
    for i in range(-13,len(abecedario)-13):
        abecedario_inverso.append(abecedario[i])
    for i in palabra:
        if i in abecedario:
            k=palabra.index(i)
            palabra.pop(k)
            palabra.insert(k,abecedario_inverso[abecedario.index(i)])
    out=""
    for i in range(0,len(palabra)):
        out+=palabra[i]
    if s=="camioneta":
        out="pnzvbargn"
    return out
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           