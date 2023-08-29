def buscarTodas(a,b):
  posiciones = ""
  numero = 0
  for i in a:
   if i == b:
    if posiciones == "":
      n=str(numero)
      posiciones += n
      numero +=1
    else:
      posiciones += " "
      n=str(numero)
      posiciones += n
      numero += 1
   else:
    numero += 1
  return posiciones
      
 

if __name__ == "__main__":
    pass
           