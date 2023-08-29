# completa el código de la función
def suma_divisores(a):
    if a != 1:
        divisor = 1
        suma = 0
        for divisor in range(1,a):
           if a%divisor==0:
              suma+=divisor
              if suma == 1:
                  p = True
              else:
                  p = False
    elif a == 1:
        return 0, False

    return suma, p
       
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(suma_divisores(a))

