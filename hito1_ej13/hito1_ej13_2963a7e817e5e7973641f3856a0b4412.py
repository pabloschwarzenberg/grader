#Factores Primos
numero = int(input("Ingrese Número: "))
num=2
while num<=numero:
  if numero%num==0:
    print(num)
    numero = numero/num
  else:
    num+=1      