def decodificar(mensaje):
     pal = mensaje.split(',')
     mensaje = ""
     for x in pal:
         z = 0
         for y in x:
             z = z * 2 + int(y)
         mensaje += chr(z)
     return mensaje


if __name__ == "__main__":
     mensaje = decodificar("01101000,01101111,01101100,01100001")
     print(mensaje)