#Ordenar tres número
n1=input()
n2=input()
n3=input()
if(n1>n2):
  if (n1>n3):
    if(n2>n3):
      print(n3+","+n2+","+n1)
    else:
      print(n2+","+n3+","+n1)
  else:
    print(n2+","+n1+","+n3)
elif(n1>n3):
   print(n3+","+n1+","+n2)
else:
   if(n3>n2):
     print(n1+","+n2+","+n3)
   else:
     print(n1+","+n3+","+n2)
 
   