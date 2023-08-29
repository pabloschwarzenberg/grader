# completa el código de la función
def suma_divisores(a):
  suma=0
  for i in range(1, a): #Ciclo del número.
    if a % i == 0: #Resto de la división del número entre otro.
      suma +=i  #Suma entre los operandos.
  return suma

a = int(input("Ingresa el número: ")) 
print("La suma de sus divisores es: ") #Impresión de resultado. 
print(suma_divisores(a)) #Impresión de la definición de la función.