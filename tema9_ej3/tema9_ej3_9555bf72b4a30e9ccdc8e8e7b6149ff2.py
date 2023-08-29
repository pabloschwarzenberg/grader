def decodificar(mensaje):
    letras=mensaje.split(",")
    num=[0]*len(letras)
    for l in letras:
        a=0
        for i in range(8):
            a+=int(l[i])*2**(7-i)
        num.append(chr(a))
    lista=[]
    for i in range(len(num)):
        if num[i]!=0:
            lista.append(num[i])
    return "".join(lista)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         