#Cálculo del dígito verificador de un rut
rut = input()
serie = True
digito = len(rut)
calculo = 0

while serie:
    for i in range(2, 8):
        if digito != 0:
            calculo += int(rut[digito-1])*i
            digito -= 1

        else:
            serie = False
            
    

calculo2 = 11 - calculo%11

if calculo2 == 10:
    dv = "k"
    
elif calculo2 == 11:
    dv = 0
    
else:
    dv = calculo2
    
print("dv=", dv)