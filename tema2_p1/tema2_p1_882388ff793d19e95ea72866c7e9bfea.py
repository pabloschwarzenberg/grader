def es_primo(numero):
  if numero<2:
    return False
  elif numero==2:
    return True
  else:
    for i in range(2,numero):
      if numero % i ==0:
        return False
    return True

def es_math():
  numero=int(input("ingrese el numero"))
  resultado=es_primo(numero)

  if resultado is True:
     print("el resultado es primo")
  else:
    print("el resultado no es primo")

if __name__ == '__main__':
    es_math()