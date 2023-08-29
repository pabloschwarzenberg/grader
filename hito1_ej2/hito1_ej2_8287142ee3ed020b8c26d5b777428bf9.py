hora = int(input("Ingrese la hora (entre 0 y 23): "))
numero = input("Ingrese el número de celular (8 cifras): ")

def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
      return "CONTESTAR"
    else:
      if hora < 14:
        if numero % 1000 == 909:
          return "CONTESTAR"
      
      return "NO CONTESTAR"
    if hora >= 17 and hora <= 19 and numero // 1000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

resultado = contestar_llamada(hora, numero)
print(resultado)
