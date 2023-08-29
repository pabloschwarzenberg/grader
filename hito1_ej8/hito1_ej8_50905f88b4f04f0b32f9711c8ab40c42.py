#Descomponer un número
n=int(input("ingrese un numero:"))
miles=n//1000
centena=(n-miles*1000)//100
decena=(n-miles*1000-centena*100)//10
unidad=(n-miles*1000-centena*100-decena*10)
if decena==0:
 print(unidad,"U")
elif centena==0:
 print(decena,"D+",unidad,"U")
elif miles==0:
 print(centena,"C+",decena,"D+",unidad,"U")
else:
 print(miles,"M+",centena,"C+",decena,"D+",unidad,"U")