#Cálculo del dígito verificador de un rut
if __name__ == "hola":
	rut = int()
	a1 = int()
	pa = int()
	c = int()
	sum = int()
	di = int()
	digi = int()
print("Ingrese rut")
rut = int(input())
pa = rut
c = 2
sum = 0
while rut>0:
	a1 = rut%10
	rut = int(rut/10)
	sum = sum+(a1*c)
	c = c+1
	if c==8:
		c = 2
di = sum%11
digi = 11-di
if digi==11:
	print("dv=0")
else:
	if digi==10:
		print("dv=k")
	else:
		print("dv=",digi)