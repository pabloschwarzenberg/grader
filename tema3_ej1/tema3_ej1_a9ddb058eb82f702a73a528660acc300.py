# completa el código de la función
def suma_divisores(numero):
  suma=0
  contador=0
  for i in range(1, numero):
      if numero % i==0:
          suma+=i
  for i in range(1, suma+1):
      if numero % i==0:
          contador+=i
  if contador==2:
      return suma;True
  elif contador==1:
      return suma,True
  else:
      return suma,False
           
           
           
if __name__=="__main__":
    numero=int(input())
    print(suma_dividores(numero))