def suma_divisores(a):
    divisores = []
    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
        else:
            None
    suma = 0
    for i in divisores:
        suma += i
    if  suma == 1:
       a = True
       return (suma, a)
    else:
      a = False
      return (suma, a)

if __name__ == "__main__":
  a = int(input("Ingrese un número: "))
  suma_divisores(a)
           