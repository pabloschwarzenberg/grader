#Descomponer un número
numero= int(input("Ingrese un numero: "))

m= numero//1000
op=numero%1000
c=op//100
op2= op%100
d=op2//10
u=op2%10

if m==0:
  print(str(c),"C+",str(d),"D+",str(u), "U")
elif m==0 and c==0:
  print(str(d),"D+",str(u),"U")
elif m==0 and c==0 and d==0:
  print(str(u),"U") 
else:
  print(str(m),"M+",str(c),"C+",str(d),"D+",str(u),"U")