#Ordenar tres números
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if(a>b and a>c and b>c):
   print(str(c)+","+str(b)+","+str(a))
elif(a>b and a>c and c>b):
   print(str(b)+","+str(c)+","+str(a))
elif(b>a and b>c and c>a):
   print(str(a)+","+str(c)+","+str(b))
elif(b>a and b>c and c<a):
   print(str(c)+","+str(a)+","+str(b))
elif(c>a and c>b and a>b):
   print(str(b)+","+str(a)+","+str(c))
elif(c>a and c>b and b>a):
   print(str(a)+","+str(b)+","+str(c))
elif(a==b and b==c and b==c):
   print(str(b)+","+str(c)+","+str(a))
elif(a==b and a>c):
   print(str(c)+","+str(b)+","+str(a))
elif(a==b and a<c):
   print(str(a)+","+str(b)+","+str(c))
elif(a==c and a>b):
   print(str(b)+","+str(c)+","+str(a))
elif(a==c and a<b):
   print(str(c)+","+str(a)+","+str(b))
elif(b==c and a>b):
   print(str(b)+","+str(c)+","+str(a))
elif(b==c and a<b):
   print(str(a)+","+str(c)+","+str(b))
                                    
