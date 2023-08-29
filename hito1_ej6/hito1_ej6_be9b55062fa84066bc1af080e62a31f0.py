#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())

#ordenes posibles:(permutacion 3!=6)
#a>b>c
#a>c>b
#b>a>c
#b>c>a
#c>a>b
#c>b>a
#note que hay que expresar de -a+
if(c<=b<=a):
  print(str(c)+","+str(b)+","+str(a))
elif(b<=c<=a):
  print(str(b)+","+str(c)+","+str(a))
elif(c<=a<=b):
  print(str(c)+","+str(a)+","+str(b))
elif(a<=c<=b):
  print(str(a)+","+str(c)+","+str(b))
elif(a<=b<=c):
  print(str(a)+","+str(b)+","+str(c))
elif(b<=a<=c):
  print(str(b)+","+str(a)+","+str(c))