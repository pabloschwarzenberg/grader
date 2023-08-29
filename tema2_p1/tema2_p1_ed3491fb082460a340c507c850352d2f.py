# por favor escribe aquí tu función
a = bool

def es_primo(numero):
   if numero < 2:
      a == False
   for x in range(2,numero):
      if numero % x == 0:
         a == False
      else:
         a == True
      print(a)

if __name__ == "__main__":
     ingresa = int(input("Ingresa un numero cualquiera "))
     es_primo(ingresa)
