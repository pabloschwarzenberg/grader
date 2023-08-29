def decodificar(mensaje):
    a = mensaje.split(",")
    lista = []
    for i in a: 
        b = list(i) 
        j = 0
        for t in range(len(b)):
            j1 = (2**(7-t)) * (int(b[t]))
            j += j1
        print(j)
        print(chr(j))
        lista.append(chr(j))
    mensaje = ''.join(lista)
    
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         