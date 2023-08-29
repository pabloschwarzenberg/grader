def descomponer(numero):

  primos=[]

  for i in range(2,numero+1):

    while numero%i==0:

      print(i)

      primos.append(i)

      numero=numero/i

  return primos

 

numero=int(input())

primos=descomponer(numero)

