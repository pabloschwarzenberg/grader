#Ordenar tres números
a = input("Ingresar un numero: ")
b = input("Ingresar otro numero: ")
c = input("Ingresar otro numero: ")    
if a <= b <= c:
  print(str(a)+","+str(b)+","+str(c))
elif a <= c <= b:
  print(str(a)+","+str(c)+","+str(b))
elif c <= a <= b:
  print(str(c)+","+str(a)+","+str(b))
elif c <= b <= a:
  print(str(c)+","+str(b)+","+str(a))
elif b <= a <= c:
  print(str(b)+","+str(a)+","+str(c))
elif b >= c >= a:
  print(str(b)+","+str(c)+","+str(a))