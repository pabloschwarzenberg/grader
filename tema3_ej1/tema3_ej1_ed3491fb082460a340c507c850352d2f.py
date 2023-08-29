# completa el código de la función
def suma_divisores(a):
  suma = 0
  primo = False
  if a == 1:
    suma = 0
    return suma,primo
  else:
    for i in range(1,a):
      if (a % i) == 0:
        suma = suma + i
    if suma == 1:
       primo = True
    return suma,primo
    
if __name__ == "__main__":
  numero = int(input("Escoja su numero "))
  print(suma_divisores(numero))
           
