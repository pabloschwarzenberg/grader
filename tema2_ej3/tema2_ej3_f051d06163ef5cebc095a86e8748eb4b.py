def numero_perfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False
 
if __name__ == "__main__":
    num=eval(input("Ingrese su numero: "))
    if numero_perfecto(num):
        print("El numero {0} es perfecto".format(num))
    else:
        print("El numero {0} no es perfecto".format(num))