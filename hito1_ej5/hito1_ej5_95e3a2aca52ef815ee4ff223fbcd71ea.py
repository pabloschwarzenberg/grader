
#Obtener el dígito verificador del RUT
rut=str(input("Ingrese su rut sin el código verificador"))

if len(rut)==9:
    v1=int(rut[-1])*2
    v2=int(rut[-2])*3
    v3=int(rut[-3])*4
    v4=int(rut[-4])*5
    v5=int(rut[-5])*6
    v6=int(rut[-6])*7
    v7=int(rut[-7])*2
    v8=int(rut[-8])*3
    v9=int(rut[-9])*4
    suma = v1+v2+v3+v4+v5+v6+v7+v8+v9

if len(rut)==8:
    v1 = int(rut[-1]) * 2
    v2 = int(rut[-2]) * 3
    v3 = int(rut[-3]) * 4
    v4 = int(rut[-4]) * 5
    v5 = int(rut[-5]) * 6
    v6 = int(rut[-6]) * 7
    v7 = int(rut[-7]) * 2
    v8 = int(rut[-8]) * 3
    suma = v1+v2+v3+v4+v5+v6+v7+v8

if len(rut)==7:
    v1 = int(rut[-1]) * 2
    v2 = int(rut[-2]) * 3
    v3 = int(rut[-3]) * 4
    v4 = int(rut[-4]) * 5
    v5 = int(rut[-5]) * 6
    v6 = int(rut[-6]) * 7
    v7 = int(rut[-7]) * 2
    suma = v1+v2+v3+v4+v5+v6+v7

if len(rut)==6:
    v1 = int(rut[-1]) * 2
    v2 = int(rut[-2]) * 3
    v3 = int(rut[-3]) * 4
    v4 = int(rut[-4]) * 5
    v5 = int(rut[-5]) * 6
    v6 = int(rut[-6]) * 7
    suma = v1+v2+v3+v4+v5+v6

if len(rut)==5:
    v1 = int(rut[-1]) * 2
    v2 = int(rut[-2]) * 3
    v3 = int(rut[-3]) * 4
    v4 = int(rut[-4]) * 5
    v5 = int(rut[-5]) * 6
    suma = v1 + v2 + v3 + v4 + v5

if len(rut)==4:
    v1 = int(rut[-1]) * 2
    v2 = int(rut[-2]) * 3
    v3 = int(rut[-3]) * 4
    v4 = int(rut[-4]) * 5
    suma =v1 + v2 + v3 + v4

if len(rut)==3:
    v1 = int(rut[-1]) * 2
    v2 = int(rut[-2]) * 3
    v3 = int(rut[-3]) * 4
    suma = v1 + v2 + v3

if len(rut)==2:
    v1 = int(rut[-1]) * 2
    v2 = int(rut[-2]) * 3
    suma = v1 + v2


dv=11-(suma%11)

if 1<=dv<=9:
    print("dv= ", dv)

elif dv==11:
    print("dv=0")

elif dv==10:
    print("dv=K")


