def decodificar(mensaje):
    N=len(mensaje)
    palabra=""
    numero=""
    for i in range (N):
        p=mensaje[i]
        print(p)
        if p==",":
            entero=int(numero,base=2)
            mensajes=chr(entero)
            palabra=palabra+mensajes
            numero=""
        else:
            numero=numero+p
        if i==(N-1):
            entero=int(numero,base=2)
            mensajes=chr(entero)
            palabra=palabra+mensajes
            numero=""
    mensaje=palabra
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)