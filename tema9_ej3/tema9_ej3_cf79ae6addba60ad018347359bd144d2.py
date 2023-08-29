def decodificar(mensaje):
    c=[]
    mensaje=mensaje.split(",")
    for i in mensaje:
        a=0
        b=0
        while b<=len(i)-1:
            a=a+(int(i[b])*(2**(len(i)-(b+1))))
            b=b+1
            print(a)
        d=chr(a)    
        c.append(d)
    print(c)    
    return("".join(c))    
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)