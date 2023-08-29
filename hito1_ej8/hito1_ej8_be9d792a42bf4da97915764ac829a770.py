#Descomponer un número
num= input("Ingrese numero: ")
largo=int(len(num))

aux=""
u=""
d=""
c=""
m=""

if largo == 4:
	aux=largo
	u = num[aux-1] + "U"
	aux =aux -1
	d = num[aux-1] + "D"
	aux =aux -1
	c = num[aux-1] + "C"
	aux =aux -1
	m = num[aux-1] + "M"
	aux =aux -1
	
	impri= m + "+" + c + "+" + d + "+" + u
	print(impri)
	
if largo == 3:
	aux=largo
	u = num[aux-1] + "U"
	aux =aux -1
	d = num[aux-1] + "D"
	aux =aux -1
	c = num[aux-1] + "C"
	aux =aux -1
	
	impri= c + "+" + d + "+" + u
	print(impri)

if largo == 2:
	aux=largo
	u = num[aux-1] + "U"
	aux =aux -1
	d = num[aux-1] + "D"
	aux =aux -1
		
	impri= d + "+" + u
	print(impri)

if largo == 1:
	aux=largo
	u = num[aux-1] + "U"
	aux =aux -1
	
	impri= u
	print(impri)      