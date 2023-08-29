#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut sin digito verificador: "))
A = (rut//1%10)*2
B = (rut//10%10)*3
C = (rut//100%10)*4
D = (rut//1000%10)*5
E = (rut//10000%10)*6
F = (rut//100000%10)*7
G = (rut//1000000%10)*2
H = (rut//10000000%10)*3
suma= A+B+C+D+E+F+G+H
suma_1=suma/11
suma_2=suma-(11*int(suma_1))
suma_3=11-suma_2
if suma_3 == 11:
    print("dv=0")
elif suma_3 == 10:
    print("dv=k")
else:
    print("dv=",suma_3)      