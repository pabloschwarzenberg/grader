def decodificar(mensaje):
  mensaje_l = mensaje.split(",")
  # mensaje_l = [int(x) for x in mensaje_l]
  aux = ""
  for code in mensaje_l:
    aux += chr(int(code, 2))
  print(aux)    
  return aux

if __name__ == "__main__":
  mensaje=decodificar("01101000,01101111,01101100,01100001")
  print(mensaje)
  
  
  
  
  
