#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese rut sin el digito verificador: "))
while not(rut<=99999999 and rut>=1000000):
    rut = int(input("Error, ingrese rut de 7 a 8 digitos: "))

tur=str(rut)[::-1] #rut al reves es tur xd
print("Rut volteado:",tur)

uno=int(tur[0])*2
dos=int(tur[1])*3
tres=int(tur[2])*4
cuatro=int(tur[3])*5
cinco=int(tur[4])*6
seis=int(tur[5])*7
siete=int(tur[6])*2

if(len(tur)==8):
    ocho=int(tur[7])*3
else:
    ocho=0

suma=uno+dos+tres+cuatro+cinco+seis+siete+ocho

resto=suma%11

dv=11-resto

if(dv==10):
    dv = "k"

if(dv==11):
    dv = 0

print("dv=",dv)      