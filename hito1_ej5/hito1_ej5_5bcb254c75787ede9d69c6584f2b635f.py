#Cálculo del dígito verificador de un rut
rut=input()   
n=1
serie=2
suma=0
producto=0
while n<=len(rut):
    if serie>7:
        serie=2
    producto=int(rut[-n])*serie
    suma=suma+producto
    n+=1
    serie+=1
guion=11-suma%11
if guion==11:
    guion=0
elif guion==10:
    guion="k"
print("dv=",guion)