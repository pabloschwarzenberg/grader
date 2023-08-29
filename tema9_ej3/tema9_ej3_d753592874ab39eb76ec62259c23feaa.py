def decodificar(codigo):
    numero=codigo.split(",")
    lista=[]
    for n in numero:
        r=int(str(n),2)
        t=chr(r)
        lista.append(t)
        a="".join(lista)
    return a

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         