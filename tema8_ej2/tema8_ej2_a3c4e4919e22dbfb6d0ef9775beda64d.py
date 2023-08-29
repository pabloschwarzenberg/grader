def buscarTodas(a,b):

  save_cadena = ""
  contador = 0

  while contador != len(a):

      if a[contador] == b:

          if save_cadena == "":
              save_cadena = save_cadena + str(contador)
              contador+=1
          else:
              save_cadena = save_cadena + " " +  str(contador)
              contador+=1

      else:
          contador += 1

  return save_cadena