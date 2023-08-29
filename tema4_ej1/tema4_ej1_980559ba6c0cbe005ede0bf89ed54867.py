import random as rd
def ocultar_letras(palabra,cantidad):
    o = []
    cantidad = cantidad
    for i in range(1,cantidad +1):
        lis = len(palabra)
        x = rd.randrange(lis)
        if x not in o:
            l = list(palabra)
            l[x] = '_'
            palabra = "".join(l) 
            o.append(x)
        elif x in o:
            cantidad = cantidad 
            
    h = palabra
    return h
   
def revisar_letra(palabra_secreta,palabra,letra):
    l = list(palabra_secreta)
    l2 = list(palabra)
    if letra in palabra_secreta:
        if l.count(letra) >= 2:
            r = l.index(letra,l.index(letra) + 1)
            l2[r] = letra
            pala1 = ''.join(l2)
            return pala1
        r = l.index(letra)
        l2[r] = letra
        pala1 = ''.join(l2)
        return pala1

if __name__ == "__main__":
    pass
         