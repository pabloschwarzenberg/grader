# completa el código de la función
def suma_divisores(a):
    sumador = 0
    for i in range (1, a):
        if a % i ==0:
            sumador +=i
    es_primo = sumador == 1
    return sumador, es_primo
if __name__ == "__main__":
  a = int(input("Ingrese un número: "))
  sumador, es_primo = suma_divisores(a)
  if es_primo:
      print("El número", a,"es primo ")
  else:
      print("El número", a,"no es primo")