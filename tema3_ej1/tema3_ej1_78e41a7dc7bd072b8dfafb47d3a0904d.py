# Suma de los divisores de un número + si el numero es primo
def suma_divisores(a):
  div_acumulador=0
  # Sumar los divisores del numero
  if a < 1:
    print("Error: el numero ingresado es inválido")
  else:
    for i in range(1, a):
        if a%i==0:
            div_acumulador+=i

    # Calcular si el numero es primo
    if a == 0 or a == 1 or a == 4:
        return div_acumulador, False
    # para sacar los multiplos
    for x in range(2, int(a/2)):
        if a % x == 0:
            return div_acumulador, False
    return div_acumulador, True 

if __name__ == "__main__":
  num=int(input("Ingrese un número: "))
  print(suma_divisores(num))