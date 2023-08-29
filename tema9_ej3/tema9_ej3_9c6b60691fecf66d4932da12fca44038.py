def decodificar(mensaje):
    l_mensaje=list(mensaje)
    i=0
    while i<len(l_mensaje):
        if l_mensaje[i]=="0":
            l_mensaje.pop(i)
            l_mensaje.append(0)
        elif l_mensaje[i]=="1":
            l_mensaje.pop(i)
            l_mensaje.append(1)
        i+=1
        x=0
        lista_mensaje=[]
        while x<len(l_mensaje):
            m=l_mensaje[x]*2**7+l_mensaje[x+1]*2**6+l_mensaje[x+2]*2**5+l_mensaje[x+3]*2**4+l_mensaje[x+4]*2**3+l_mensaje[x+5]*2**2+l_mensaje[x+6]*2**1+l_mensaje[x+7]*2**0
            lista_mensaje.append(m)
            x=x+9
        q=0
        mensaje=0
        while q<len(lista_mensaje):
            mensaje=mensaje+chr(lista_mensaje[q])
            
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         