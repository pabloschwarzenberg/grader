#Factores Primos
num = int(input("Ingrese un número: "))

for n in range(2,num+1):
 esPrimo = False
 if(num % n == 0):
      if(n == 2):
           esPrimo = True
      else:
           esPrimo = True

           for m in range(2,n):
                if(n % m == 0):
                    esPrimo = False

 if(esPrimo):
  print(n)
