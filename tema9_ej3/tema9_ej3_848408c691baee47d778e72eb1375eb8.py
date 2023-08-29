def decodificar(mensaje):
     res = mensaje.split(',')
     mensaje = ""
     for i in res:
         decimal = 0
         for each in i:
             decimal = decimal * 2 + int(each)
         mensaje += chr(decimal)
     return mensaje


if __name__ == "__main__":
     mensaje = decodificar("01101000,01101111,01101100,01100001")
     print(mensaje)