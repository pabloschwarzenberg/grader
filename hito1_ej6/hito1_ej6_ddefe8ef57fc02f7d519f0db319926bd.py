#Ordenar tres números
a = int(input("ingrese primer numero "))
b = int(input("ingrese segundo numero "))
c = int(input("ingrese tercer numero "))

if( a<b and a<c):
     if (b<c):
        print ( str(a) + (","), str(b) + (","), c)
     else:
        print ( str(a) + (","), str(c) + (","), b)
elif(b<a and b<c):
      if (a<c):
        print ( str(b) + (","), str(a) + (","), c)
      else:
        print ( str(b) + (","), str(c) + (","), a)
elif (c<a and c<b):
      if (a<b):
        print ( str(c) + (","), str(a) + (","), b)
      else:
        print ( str(c) + (","), str(b) + (","), a)