#Cálculo del dígito verificador de un rut
rut = input("ingrese los 8 primeros digitos de su rut:")
inw = len(rut)
por = 1
suma = 0
for x in range (inw-1,-1,-1):
    por = por+1
    suma = suma + int(rut[x])*por
    #print(int(rut[x])*por)
    if por == 7:
        por = 1
modu = suma//11
entero = suma-(11*modu)
total = 11 - entero
print(modu)
print(entero)
print(total)
if total == 11:
    print("dv=0")
elif total <10:
    print("DV=",total)
elif total == 10:
    print("DV=K")