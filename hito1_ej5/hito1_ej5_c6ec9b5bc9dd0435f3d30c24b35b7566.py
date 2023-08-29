rut=input("Ingrese su rut sin el digito verificador: ")
rutk=list(reversed(rut))
posicion=0
caca=2
pipi=0
while posicion<len(rutk):
    christiantemeo=rutk[posicion]
    lucasgey=int(christiantemeo)
    if caca==8:
        caca=2
    resultado=lucasgey*caca
    caca+=1
    posicion+=1
    pipi=resultado+pipi
xd=pipi//11
popo=xd*11
resultadofinal=pipi-popo
sodastereo=11-resultadofinal
if sodastereo==11:
    sodastereo=0
elif sodastereo==10:
    sodastereo="k"
else:
    sodastereo=sodastereo
print("dv=",sodastereo)