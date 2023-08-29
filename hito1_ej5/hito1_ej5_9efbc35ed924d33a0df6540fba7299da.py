#Cálculo del dígito verificador de un rut
#calculo digito verificador de Rut chile
nRut=str(int(input("Ingrese su numero de Rut")))
form= "32765432"
i=1
suma=0
for x in str(nRut):
    suma= suma + int(nRut[-i]) * int(form[-i])
    i+=1
    
digVer= 11-int(suma%11)
if digVer==11:
    digVer=0
elif digVer==10:
    digVer='k'
print ("dv = ",digVer)
  