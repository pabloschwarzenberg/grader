def decodificar(mensaje):
    mensaje=mensaje.split(",")
    lista=[]
    for numero in mensaje:
        numero=numero[::-1]
        cont=0
        print(numero)
        n=0
        for i in numero:
            n+=int(i)*2**(cont)
            print(n)
            cont+=1
        lista.append(n)
    s=""
    for numero in lista:
        s+=chr(numero)
        
    return s
        

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
