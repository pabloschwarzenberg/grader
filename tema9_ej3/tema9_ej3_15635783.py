def decodificar(mensaje):
    resultado=[]
    mensaje=mensaje.split(",")
    for i in mensaje:
        x=list(i)
        x.reverse()       
        letra=[]
        print(x)
        r=0
        for n in x:
            n=int(n)
           
            k=int(n)*int((2**int(r)))
            print(k)
            letra.append(int(k))
            r=r+1
        suma_letra=sum(letra)
        resultado.append(chr(suma_letra))
        
    resultado=("").join(resultado)
    return resultado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         