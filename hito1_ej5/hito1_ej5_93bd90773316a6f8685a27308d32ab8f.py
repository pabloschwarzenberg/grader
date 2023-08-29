#Digito verificador
rut = int(input("Ingrese su rut: "))
#operaciones
d1 = (rut//10000000)%10
d2 = (rut//1000000)%10
d3 = (rut//100000)%10
d4 = (rut//10000)%10
d5 = (rut//1000)%10
d6 = (rut//100)%10
d7 = (rut//10)%10
d8 = (rut//1)%10
#verificador
m1 = d1*3
m2 = d2*2
m3 = d3*7
m4 = d4*6
m5 = d5*5
m6 = d6*4
m7 = d7*3
m8 = d8*2
#suma
suma = m1+m2+m3+m4+m5+m6+m7+m8
division = suma//11
rDivision = suma - (11*division)
rFinal = 11 - rDivision
#print(rFinal)
if rFinal == 11:
    print("dv=0")
if rFinal == 10:
    print("dv=K")
elif rFinal < 10:
    print("dv=",rFinal)
      