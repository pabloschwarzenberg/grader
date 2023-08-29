# completa el código de la función
def numero_perfecto(a):
  cont = 0
  suma_cont=0
  lista=[]
  for divisor in range(1,a+1):
   if (a % divisor) == 0 :
     print(divisor,"es divisor")
     lista.append(divisor)
     print(lista)
     cont += 1
  if 1+1==2:
    lista.pop(-1)
  print(lista)

  suma=sum(lista)
  if 2*2==4:
    suma
    print(suma)
    suma_cont+=1


  if suma == a:
   primo = True
  else:
    primo = False

  return primo
