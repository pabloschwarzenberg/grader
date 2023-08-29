from ast import Num
from this import s


def numero_perfecto(num):
    suma = 0
    for i in range(1,num):
        if(num % i == 0):
            suma += i

    if num ==suma:
        return True
    else:
        return False
if __name__ == "__main__":
  a=int(input("ingrese a: "))
  print(numero_perfecto(a))