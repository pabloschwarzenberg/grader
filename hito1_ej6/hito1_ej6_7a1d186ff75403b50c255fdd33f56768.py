#Ordenar tres números
a = int(input("ingrese un numero para a "))
b = int(input("ingrese un numero para b "))
c = int(input("ingrese un numero para c "))

if a<b<c or a<=b<=c or a<b<=c or a<=b<c:
  print(a,b,c)
elif a<c<b or a<=c<=b or a<c<=b or a<=c<b:
  print(a, c, b)
elif b<a<c or b<=a<=c or b<a<=c or b<=a<c:
  print(b, a, c)
elif b<c<a or b<=c<=a or b<c<=a or b<=c<a:
  print(b, c, a)
elif c<a<b or c<=a<=b or c<a<=b or c<=a<b:
  print(c, a, b)
elif c<b<a or c<=b<=a or c<b<=a or c<=b<a:
  print(c, b, a) 