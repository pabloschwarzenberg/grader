# completa el código de la función
def suma_divisores(n):
    global suma
    global lista
    suma = 0
    lista = []
    numero = int(n)
    for i in range(1, numero):
        if numero % i == 0:
            lista.append(i)
        i += 1
    for divisor in lista:
        suma += divisor
    if suma == 1:
      return (1, True)
    else:
      return (suma, False)

if __name__ == "__main__":
  n = input()
  suma_divisores(n)
  print("(",suma, primo,")") 