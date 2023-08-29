# completa el código de la función
def suma_divisores(n):
    suma=0
    for i in range (1,n):
        if (n%i==0):
            suma=suma+i
    return (suma),suma==1
if __name__=="__Main__":
  a=int(input("Ingrese un número"))
  print("La suma de los divisores es:",suma_divisores(a))
  if suma_divisores(a)==1:
    print("El número es primo")
  else:
    print("El número no es primo")
  