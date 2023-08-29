#Cálculo del dígito verificador de un rut
#DÍGITO VERIFICADOR
#INPUT
rut=int(input("Ingresa tu RUT sin el dígito verificador: "))
#CÁLCULO DEL DÍGITO VERIFICADOR
d8=rut//10000000
d8=d8*3
d7=rut%10000000
d7=d7//1000000
d7=d7*2
d6=rut%1000000
d6=d6//100000
d6=d6*7
d5=rut%100000
d5=d5//10000
d5=d5*6
d4=rut%10000
d4=d4//1000
d4=d4*5
d3=rut%1000
d3=d3//100
d3=d3*4
d2=rut%100
d2=d2//10
d2=d2*3
d1=rut%10
d1=d1//1
d1=d1*2
sp=d1+d2+d3+d4+d5+d6+d7+d8
resto1=sp//11
resto2=sp-(11*resto1)
resto3=11-resto2
#OUTPUT
if resto3==11:
	print("dv=0")
elif resto3==10:
	print("dv=k")
else:
	print("dv=",resto3)