#Ordenar tres números
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Ingrese otro numero: "))

if a<=b<=c :
  print(str(a)+","+str(b)+","+str(c))
elif a<=c<=b :
  print(str(a)+","+str(c)+","+str(b))
elif b<=c<=a :
  print(str(b)+","+str(c)+","+str(a))
elif b<=a<=c :
  print(str(b)+","+str(a)+","+str(c))
elif c<=b<=a :
  print(str(c)+","+str(b)+","+str(a))
elif c<=a<=b :
  print(str(c)+","+str(a)+","+str(b))

elif c<=a<=b :
  print(c,a,b)