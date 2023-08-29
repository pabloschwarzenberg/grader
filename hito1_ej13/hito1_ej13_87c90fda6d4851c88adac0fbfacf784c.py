#debe retornar 1 si es primero y 0 si no lo es
def comprobarPrimo(y):
  salida = 1
  #debe haber un ciclo que verifique que el número "y", sólo es divisible por 1 y por "y"
  for i in range(2,y):
    if(y % i == 0):
      salida = 0
  return salida


#imprime los factores primos de un número
def factoresPrimos(x):
  for i in range(2,x+1):
    if(x % i == 0 and comprobarPrimo(i) == 1):
      print(i)
  #debe haber un ciclo que revise si cada número (i) que le precede es divisor de X, y además es primo, lo mostrará por pantalla
  #x % i == 0, si eso es cierto (el resto del número divido)



factoresPrimos(eval(input()))