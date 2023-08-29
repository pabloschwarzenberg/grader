def numero_perfecto(numero):
  contador = 1
  suma = 0
  while contador != numero:
    if numero % contador == 0:
      suma = suma + contador
    contador = contador + 1
  if suma == numero:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           