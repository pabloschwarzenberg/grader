#Factores Primos
#Un número es primo si puedes ser dividido por 1 y por si mismo. El 1 no es primo
n = int(input("Ingrese un número: "))

esPrimo = True

if n==1:
          print("NO es primo")
          elif:
          divisor = 2
          while divisor < n:
            if n % divisor == 0:
              esPrimo = False
            divisor = divisor + 1

          if esPrimo:
            print("Es primo")
          else:
            print("No es primo")
elif:
          if n<0:
                    print("no es")