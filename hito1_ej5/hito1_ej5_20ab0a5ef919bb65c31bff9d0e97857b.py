#Cálculo del dígito verificador de un rut
num=int(input("Ingrese un numero para culacular su digito verificador: "))
snum=list(str(num))
suma=0
n=2
for i in range(len(snum)):
    suma=suma+(n*int(snum[(len(snum)-i-1)]))
    n+=1
    if n>7:
        n=2
        
resto=11-suma%11

if((resto)==10):
    dv="K"
else:
    if((resto)==11):
        dv="0"
    else:
        dv=str(resto)
    
print("dv="+dv)     