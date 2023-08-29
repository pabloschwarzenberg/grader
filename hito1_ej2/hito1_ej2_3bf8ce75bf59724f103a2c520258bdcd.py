n= int(input("Ingrese un número telefónico:"))
h= int(input("Ingrese la hora de la llamada:"))
ns=str(n)
a=ns[0:3]
b=ns[5:8]
print("Los últimos números son:",b)
c=909
c=str(c)
d=877
d=str(d)
if 0<=h<=7:
    print("CONTESTAR")
elif 7<h<14:
      if b==c:
       print("CONTESTAR")
      else:
       print("NO CONTESTAR")
elif 14<=h<17:
     print("NO CONTESTAR")
elif 17<=h<=19:
      if a==d:
        print("NO CONTESTAR")
      else:
        print("CONTESTAR")
elif h>19:
    print("NO CONTESTAR")