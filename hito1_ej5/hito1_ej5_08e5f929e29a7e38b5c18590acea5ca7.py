import math
rut = int(input("ingrese su rut: "))
rut1 = rut%10
rut2 = (rut%100)//10
rut3 = (rut%1000)//100
rut4 = (rut%10000)//1000
rut5 = (rut%100000)//10000
rut6 = (rut%1000000)//100000
rut7 = (rut%10000000)//1000000
rut8 = (rut%100000000)//10000000
multi = (rut1*2+rut2*3+rut3*4+rut4*5+rut5*6+rut6*7+rut7*2+rut8*3)
divi = multi//11
resto = multi - (11*divi)
identificador = 11 - resto
if identificador==11:
    print("dv=0")
if identificador==10:
    print("dv=K")
if identificador<=9:
    print("dv=",identificador)