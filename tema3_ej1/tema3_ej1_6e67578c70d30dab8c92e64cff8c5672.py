# completa el código de la función
def suma_divisores(a):
    suma = 0
    if (a==1):
      return suma
    else:
      for i in range(1, a):
        if (a % i == 0):
          suma += i
             
      if (suma == 1):
        return suma
      else:
        return suma
     
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(suma_divisores(a))