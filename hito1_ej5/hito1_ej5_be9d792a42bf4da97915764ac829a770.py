#Cálculo del dígito verificador de un rut

rut=input("Ingrese el Rut sin Digito Verificador: ")
cont= 0
serie = 2
largo=len(rut)
acumulado=0
while cont < largo:
	aux = int(rut[largo - (cont + 1)])
	
	if serie <= 7:
		acumulado = acumulado + (serie * aux)
	else:
		serie = 2
		acumulado = acumulado + (serie * aux)
		
	cont = cont + 1 
	serie = serie + 1

mod=acumulado%11
mod=11-mod
dv=""
if mod == 11:
	dv=0
elif mod == 10:
	dv="K"
else:
	dv=str(mod)

print("dv=",dv)
      