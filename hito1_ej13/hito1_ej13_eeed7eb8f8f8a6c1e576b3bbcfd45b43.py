#Factores Primos
var_NumeroEntero = int(input("Ingrese un número entero: "))
var_FactorPrimo = 2
while (var_FactorPrimo <= var_NumeroEntero):
   if (var_NumeroEntero % var_FactorPrimo == 0):
       print(var_FactorPrimo)
       var_NumeroEntero = var_NumeroEntero / var_FactorPrimo
   else:
       var_FactorPrimo += 1