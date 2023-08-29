#Descomponer un número
numero=(int(input("Ingrese un número de hasta 4 dígitos\n")))
um=0
c=0
d=0
u=0
um=numero//1000
c=((numero-(um*1000))//100)
d=(numero-(um*1000+c*100))//10
u=(numero-(um*1000+c*100+d*10))
if(um>0):
  print (um,"M", "+",c,"C","+",d,"D","+",u,"U")
elif um==0 and c!=0:
  print (c,"C","+",d,"D","+",u,"U")
elif c==0 and um ==0 and d!=0:
  print (d,"D","+",u,"U")
elif d==0 and c==0 and um==0:
  print (u,"U")