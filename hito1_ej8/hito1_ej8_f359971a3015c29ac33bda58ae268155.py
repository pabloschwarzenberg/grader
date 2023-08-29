#Descomponer un número
numero1 = int(input("Ingrese un numero de hasta 4 cifras: "))
miles= int((numero1 - (numero1%1000)))
m=int(miles/1000)
res1=numero1-miles
centenas= res1-(numero1%100)
c= int(centenas/100)
res2=res1-centenas
decenas= res2-(numero1%10)
d=int(decenas/10)
res3= res2-decenas
unidades= res3  -(numero1%1)
u=int(unidades/1)
if m==0 and c>=1 and d>=0 and u>=0:
    print(c,"C","+",d,"D","+",u,"U")
elif m==0 and c==0 and d>=1 and u>=0:
    print(" {{d}D+{u}U")
elif m>=1 and c>=0 and d>=0 and u>=0:
    print(m,"M","+",c,"C","+",d,"D","+",u,"U")
elif m==0 and c==0 and d>=1 and u>=0:
    print(d,"D","+",u,"U")
elif m==0 and c==0 and d==0 and u>=1:
    print(u,"U")
   