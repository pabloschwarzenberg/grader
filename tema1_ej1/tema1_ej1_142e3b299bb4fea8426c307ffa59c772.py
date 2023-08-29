#Suma de los N primeros números
def suma(n):
  suma=n*(n+1)/2
  return(suma)

numero=int(input("ingrese un numero"))
resultado= suma(numero)
print("la suma entre", (numero), "da como resultado", (resultado))   