#La mitad del código está muy extraño, pero funciona y es lo que importa. Disculpe profe#
rutnum=str(input("ingrese rut: "))
cont=0
rut = [int(x) for x in reversed(rutnum)]
rut.insert(0, 0)
rut.insert(1, 0)

while cont<7:
    for n in range(0,8):
        rut[n]=rut[n]*n
        cont=cont+1
rut[8]=rut[8]*2
try:
    rut[9]=rut[9]*3
except IndexError:
    pass  
suma=sum(rut)
resto=suma%11
fin=11-resto
if fin==11:
    print("dv=0")
elif fin==10:
    print("dv=k")
else:
    print("dv=",fin)
