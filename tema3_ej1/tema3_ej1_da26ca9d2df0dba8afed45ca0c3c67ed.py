# completa el código de la función
def suma_divisores (a):
    sumador = 0
    for i in range(1,a + 1,1):
        if a%i == 0:
            sumador = sumador + i
    b = sumador - a
    if b%b == 0 and b%1 == 0:
        return True
    else:
        return False
 
if __name__ == "__main__":
  numero = int(input('Ingrese numero: '))
  suma_divisores(numero)
  if suma_divisores == True:
    print('el numero es primo')
  else:
    print('el numero no es primo')