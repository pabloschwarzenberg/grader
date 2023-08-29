# por favor escribe aquí tu función
def es_primo(numero):
  return
def es_primo(numero):
  if numero <= 1:
    return False
  elif numero == 2:
    return True
  else:
    for i in range(2, numero):
      if numero % i == 0:
        return False #retorna False si el numero es divisible por cualquier otro numero que no sea el recibido
    return True #termina el For, quiere decir que el numero solo es divisible por si mismo

if __name__ == "__main__":
  numero = int(input('Ingrese un número: '))
  respuesta = es_primo(numero)
  if respuesta == True:
    print('¡El número '+str(numero)+' es primo!')
  else:
    print('El número '+str(numero)+' no es primo')           