a=(int(input("ingrese un numero:")))
b=(int(input("ingrese un numero:")))
c=(int(input("ingrese un numero:")))
lista=c,b,a
lista2=b,c,a
lista3=c,a,b
lista4=a,c,b
lista5=a,b,c
lista6=b,a,c
if(c<b<a):
  print(list(lista1))
elif(b<=c<=a):
  print(list(lista2))
elif(c<=a<=b):
  print(list(lista3))
elif(a<=c<=b):
  print(list(lista4))
elif(a<=b<=c):
  print(list(lista5))
elif(b<=a<=c):
  print(list(lista6))