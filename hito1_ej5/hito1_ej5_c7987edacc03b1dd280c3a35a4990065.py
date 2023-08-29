rut=int(input("ingrese rut sin digito verificador: "))
#sin digito verificador
while rut<1000000 or rut >99999999:
    rut=int(input("ERROR, ingrese nuevamente su rut sin digito verificador: "))
# 18162098
sumatoriadigitos= ((rut%10)*2)
sumatoriadigitos1 = (rut%100)
sumatoriadigitos11=(sumatoriadigitos1//10)*3
sumatoriadigitos2 = (rut%1000)
sumatoriadigitos22= (sumatoriadigitos2//100)*4
sumatoriadigitos3=(rut%10000)
sumatoriadigitos33=(sumatoriadigitos3//1000)*5
sumatoriadigitos4=(rut%100000)
sumatoriadigitos44=(sumatoriadigitos4//10000)*6
sumatoriadigitos5=(rut%1000000)
sumatoriadigitos55=(sumatoriadigitos5//100000)*7
sumatoriadigitos6=(rut%10000000)
sumatoriadigitos66=(sumatoriadigitos6//1000000)*2
sumatoriadigitos7=(rut%100000000)
sumatoriadigitos77=(sumatoriadigitos7//10000000)*3

S=(sumatoriadigitos77+sumatoriadigitos66+sumatoriadigitos55+sumatoriadigitos44+sumatoriadigitos33+sumatoriadigitos22+sumatoriadigitos11+sumatoriadigitos)
division=(S//11)
operacion=(S-(11*division))
dv=(11-operacion)

if dv == 11:
    print("dv=0")
elif dv == 10:
    print("dv="+str ("K"))
else:
    print("dv="+str(dv))