# completa el código de la función
def suma_divisores(numero):
    #numero 6
    #divisores 1, 2 y 3
    #numero 7
    #divisor 1
    suma = 0
    for x in range(1,numero):
      if numero%x==0:
        suma=suma+x
    if suma==1:
      return suma, True
    else:
      return suma, False

if __name__ == "__main__":
  b=int(input("Ingrese numero"))
  print(suma_divisores(b))
           