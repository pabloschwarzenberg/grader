rut=input("ingrese su rut sin digito verificador: ")
num1=''
num2=''
num3=''
num4=''
num5=''
num6=''
num7=''
num8=''
suma=''
division=''
rdivision=''
total=''
dv=''
if rut==rut[0]+rut[1]+rut[2]+rut[3]+rut[4]+rut[5]+rut[6]:
    rut=rut[0]+rut[1]+rut[2]+rut[3]+rut[4]+rut[5]+rut[6]
    num1 = int(rut[0])* 2
    num2 = int(rut[1])* 7
    num3 = int(rut[2])* 6
    num4 = int(rut[3])* 5
    num5 = int(rut[4])* 4
    num6 = int(rut[5])* 3
    num7 = int(rut[6])* 2
    suma = num1 + num2 + num3 + num4 + num5 + num6 + num7
    division =int((suma)/11)
    rdivision =int(suma)-(11 * division)
    total = round((11) - (rdivision))
    if total==11:
        dv=0
    elif total==10:
        dv='k'
    else:dv=total
elif rut == rut[0] + rut[1] + rut[2] + rut[3] + rut[4] + rut[5] + rut[6] + rut[7]:
    rut = rut[0] + rut[1] + rut[2] + rut[3] + rut[4] + rut[5] + rut[6] + rut[7]
    num1 = int(rut[0]) * 3
    num2 = int(rut[1]) * 2
    num3 = int(rut[2]) * 7
    num4 = int(rut[3]) * 6
    num5 = int(rut[4]) * 5
    num6 = int(rut[5]) * 4
    num7 = int(rut[6]) * 3
    num8 = int(rut[7]) * 2
    suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
    division =int((suma)/11)
    rdivision =int(suma)-(11 * division)
    total = round((11) - (rdivision))
    if total==11:
        dv=0
    elif total==10:
        dv='k'
    else:dv=total
print("dv=", dv)
