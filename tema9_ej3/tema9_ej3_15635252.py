def decodificar(mensaje):
    code=mensaje.split(",")
    salida=[]
    for letra in code:
      indice=chr(int(letra,2))
      salida.append(indice)
    salida="".join(salida)
    return salida

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         