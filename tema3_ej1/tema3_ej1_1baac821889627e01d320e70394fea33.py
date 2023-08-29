# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    return suma


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
if (suma_divisores(a))== 1:
  print("Este numero es un numero primo, la suma de sus devisores es = 1")

           