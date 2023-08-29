# por favor escribe aquí tu función
def es_primo(numero):
  if numero==2 or numero==3 or numero==5 or numero==7:
      return True
  else:
      if numero%2==0 or numero%3==0 or numero%5==0 or numero%7==0 or numero==1:
        return False
      else:
        return True
#n=int(input("Ingresa el posible número primo: "))
#primo= es_primo(n)
#print(primo)