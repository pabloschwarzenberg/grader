#Cálculo del dígito verificador de un rut
#Dígito verificador
n = int(input("ingrese su rut: "))

u = n // 1%10
d = n // 10%10
c = n // 100%10
um = n // 1000%10
dm = n // 10000%10
cm = n // 100000%10
umill = n // 1000000%10
dmill = n // 10000000%10

#25724661

n1=u*2
n2=d*3
n3=c*4
n4=um*5
n5=dm*6
n6=cm*7
n7=umill*2
n8=dmill*3


Suma = (n1+n2+n3+n4+n5+n6+n7+n8)
resto1= Suma//11
resto2=Suma-(11*resto1)
resta=11-resto2
if resta == 11:
	print("dv=",end= "")
	print(0)
elif resta == 10:
	print("dv=",end= "")
	print("k")
else:
	print ("dv=",end= "")
	print(resta)      