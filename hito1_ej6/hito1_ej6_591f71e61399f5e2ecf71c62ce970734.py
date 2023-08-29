a = int(input("Escriba un numero a "))
b = int(input("Escriba un numero b "))
c = int(input("Escriba un numero c "))   

if a <= b <= c:
  print(str(a)+","+str(b)+","+str(c))
elif a <= c <= b:
  print(str(a)+","+str(c)+","+str(b))
elif c <= a <= b :
  print(str(c)+","+str(a)+","+str(b))
elif b <= a <= c:
  print(str(b)+","+str(a)+","+str(c))
elif b <= c <= a:
  print(str(b)+","+str(c)+","+str(a))
elif c <= b <= a :
  print(str(c)+","+str(b)+","+str(a))
