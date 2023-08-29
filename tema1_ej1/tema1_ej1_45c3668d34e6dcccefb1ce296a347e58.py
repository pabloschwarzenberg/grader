#Suma de los N primeros números
def suma_n_primeros_numeros(n):
  suma=n+1
  resultado=n*suma
  resultado2=int(resultado/2)
  return resultado2
numero=int(input("ingres un numero:"))
print(suma_n_primeros_numeros(numero))