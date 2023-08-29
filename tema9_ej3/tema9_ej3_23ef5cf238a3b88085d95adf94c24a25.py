def decodificar(mensaje):
    t = mensaje.split(",")
    output = ""
    for i in t:
      letradec = int(i,2)
      letra = chr(letradec)
      output += letra
    return output

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         