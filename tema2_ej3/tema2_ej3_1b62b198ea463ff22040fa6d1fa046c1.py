def numero_perfecto(a):
    suma = 0
    for i in range(1,a):
       if (a%(i)==0):
          suma+=(i)
    if a==suma:
       return True
    else:
       return False
if __name__ == "__main__":
    numero=eval(input("Ingrese su numero: "))
    if numero_perfecto(numero):
        print("El numero {0} es perfecto",numero_perfecto(numero))
    else:
        print("El numero {0} no es perfecto",numero_perfecto(numero))