#Cálculo del dígito verificador de un rut
rut = eval(input("Ingrese el rut: "))
rutstr = str(rut)
dv = 0
digito = 0
n = 0
for i in range(len(rutstr)):
    if n > 5:
        n = 0
    
    digito += int(rutstr[len(rutstr) - i - 1:len(rutstr) - i]) * (2+n)
    n += 1
    
    
        
digito = digito%11
dv = 11 - digito
    
if dv < 10:
    print("dv=",dv)
    
if dv == 10:
    print("dv=k")
    
if dv == 11:
    print("dv=",0)