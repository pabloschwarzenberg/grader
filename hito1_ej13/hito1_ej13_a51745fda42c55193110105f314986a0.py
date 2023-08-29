#Factores Primos
def factorizar(n):
   numeros_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
   numero_primo_actual = next(numeros_primos)
   resultado = []
   cociente = None
   while cociente != 1:
      if n % numero_primo_actual != 0:
         numero_primo_actual = next(numeros_primos)
         continue
      resultado.append(numero_primo_actual)
      n = cociente = n / numero_primo_actual
   return resultado

n = int(input("Ingresa un número: "))
factores = factorizar(n)
print(factores)

#print("[" + ", ".join(map(str, factores)) + "]")