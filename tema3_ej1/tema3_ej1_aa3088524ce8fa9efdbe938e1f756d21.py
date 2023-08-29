# completa el código de la función
def suma_divisores(numero):
  suma = 0
  for i in range(1,numero):
    if numero % i==0:
      suma += i 
  es_primo= suma == 1
  return suma, es_primo
           
#principal
if __name__ == "__main__":
  numero= int(input("ingrese un numero: "))
  resultado, es_primo = suma_divisores(numero)
  print("La suma de los divisores de", numero, "es:", resultado)
  if es_primo:
    print(numero, "es primo.")
  else:
    print(numero, "no es primo.")