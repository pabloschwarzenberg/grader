serie = [2,3,4,5,6,7,2,3]
rut = str(input("Ingrese su RUT: "))
suma = 0
ind = 0
for i in reversed(rut):
	print(i, " x ", serie[ind])
	suma += int(i) * serie[ind]
	ind += 1

dv = 11 - suma % 11

if dv == 11:
	dv = 0
elif dv == 10:
	dv = "K"

print("dv = ", dv)