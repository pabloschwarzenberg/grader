def decodificar(mensaje):
    mensaje=mensaje.split(",")
    lista=[]
    for letra in mensaje:
      lista.append(str(chr(int(letra,2))))
    lista="".join(lista)
    return lista
      
      

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    "".join(mensaje)
    print(mensaje)
         