# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma==1:
      a=suma,True
      return a
    else:
      b=suma,False
      return b
    
    
if __name__ == "__main__":
  numero = int(input("Ingresa el número: "))
  print(suma_divisores(numero))