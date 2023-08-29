#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if(a<=b<=c):
   print("{},{},{}".format(a,b,c))
elif(b<=c<=a):
   print("{},{},{}".format(b,c,a))
elif(c<=a<=b):
   print("{},{},{}".format(c,a,b))
elif(a<=c<=b):
   print("{},{},{}".format(a,c,b))
