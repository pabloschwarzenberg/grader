rut = input("ingrese rut :")
new_rut = ((rut[::-1]))
suma = 0
if len(new_rut) == 8 :
    v1 = int(new_rut[0])*2
    v2 = int(new_rut[1])*3
    v3 =  int(new_rut[2])*4
    v4 =  int(new_rut[3])*5
    v5 =  int(new_rut[4])*6
    v6 =  int(new_rut[5])*7
    v7 =  int(new_rut[6])*2
    v8  =  int(new_rut[7])*3
    suma =  v1+v2+v3+v4+v5+v6+v7+v8
elif len(new_rut) == 7 :
    v1 = int(new_rut[0]) * 2
    v2 = int(new_rut[1]) * 3
    v3 = int(new_rut[2]) * 4
    v4 = int(new_rut[3]) * 5
    v5 = int(new_rut[4]) * 6
    v6 = int(new_rut[5]) * 7
    v7 = int(new_rut[6]) * 2
    suma = v1+v2+v3+v4+v5+v6+v7
#print(suma)
div = suma//11
#print(div)
mult = div*11
#print(mult)
nose = suma-mult
#print(mult)
alo = 11 - nose
#print(alo)
if alo <= 9 :
    print("dv = "+str (alo))
if alo == 10 :
    print("dv = k")
if alo == 11 :
    print("dv = 0")
