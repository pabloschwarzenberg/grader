# completa el código de la función
def suma_divisores(a):
  divisor=1
  suma=0
  for i in range(1,a):
      if a%divisor==0:
          suma+=divisor
      divisor+=1
  if suma==1:
      esprimo=True
      return suma,esprimo
  else:
      esprimo=False
      return suma,esprimo
if __name__ == "__main__":
  a=int(input("Ingrese el número: "))
  print("La suma de los divisores de",a,"junto con el carácter primo del número es:",suma_divisores(a))
           