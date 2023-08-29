def decodificar(mensaje):
    l=[]
    s=0
    n=-1
    e=7
    
    for i in mensaje:
        l.append(i)
    mensaje=""
    
    while n<len(l):
        n=n+1
        suma=0
        e=7
        
        while l[n]!=",":
            l[n]=int(l[n])
            s=l[n]*2**e
            e=e-1
            suma=suma+s
            n+=1
            if n==len(l):
                break
        letra=chr(suma)
        mensaje=mensaje+letra
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)