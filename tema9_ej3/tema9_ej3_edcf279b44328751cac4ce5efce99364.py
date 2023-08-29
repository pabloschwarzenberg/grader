def decodificar(mensaje):
     partes = mensaje.split(",")
     respuesta = ""
     for parte in partes:
           respuesta += chr(int(parte,2))
     return respuesta

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         