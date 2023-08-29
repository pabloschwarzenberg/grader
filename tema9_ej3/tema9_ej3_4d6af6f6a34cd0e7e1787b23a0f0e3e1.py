def decodificar(mensaje):
    lista=[]
    s=0
    n=-1
    exponente=7
    
    for i in mensaje:
        lista.append(i)
    mensaje=""
    
    while n<len(lista):
        n=n+1
        suma=0
        exponente=7
        
        while lista[n]!=",":
            lista[n]=int(lista[n])
            s=lista[n]*2**exponente
            exponente=exponente-1
            suma=suma+s
            n+=1
            if n==len(lista):
                break
        letra=chr(suma)
        mensaje=mensaje+letra
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
         