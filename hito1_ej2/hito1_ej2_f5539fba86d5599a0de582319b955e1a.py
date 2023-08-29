#Contestador de celular
c=int(input()) 
h=int(input())
if 0<=h<=7:
 print("CONTESTAR")
elif 7<=h<14:
   x=(c%10)
   e=(x%10)
   y=(e%10)
   resultado1=(x*100+e*10+y)
    if resultado1=909:
    print("CONTESTAR)
   else:
     print("NO CONTESTAR")
elif 17<=h<=19:
    print("CONTESTAR")
    else:
    x1=(c//100000000)
    x2=(c%100000000)
    e1=(x2//10000000)
    e2=(x2%10000000)
    y1=(e2//1000000)
    y2=(e2%1000000)
    resultado2=(x1*100+e1*10+y1)
     if resultado2=877:
      print("NO CONTESTAR")
else: 
   h>19
   print("NO CONTESTAR")  