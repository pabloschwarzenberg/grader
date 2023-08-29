#Numeros perfectos
def numero_perfecto(num):
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma += i
    if num == suma:
        return True
    else:
        return False
if __name__ == "__main__":
  num = int(input("introduzca un numero:"))
  if numero_perfecto(num):
    print("%s es un numero perfecto" % num)
  else:
    print("%s NO es un numero perfecto" % num)