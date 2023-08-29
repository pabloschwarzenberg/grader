def digitos(num):
    dig=1
    while num/10>1:
        dig+=1
        num=num/10
    return dig
def decodificar(mensaje):
    palabra=[]
    mensaje=mensaje.split(",")
    for i in mensaje:
        sum=0
        cont=1
        for j in i:
            if j=="1":
                k=(len(i)-cont)
                num=2**k
            else:
                num=0
            sum+=num
            cont+=1
        letra=chr(sum)
        palabra.append(letra)
    mensaje="".join(palabra)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         