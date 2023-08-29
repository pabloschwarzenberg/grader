def numero_perfecto(a):
    suma = 0
    for i in range(1,a):
        if a%i == 0:
            suma += i
    if suma==a:
        return True
    else:
        return False
if __name__ == "__main__":
  x = int(input("Ingrese su numero: "))
  if numero_perfecto(x):
    print("El numero {0} es perfecto".format(x))
  else:
    print("El numero {0} no es perfecto".format(x))