rut=int(input("Ingrese su rut sin digito verificador: "))
A = (rut//1%10)*2
B = (rut//10%10)*3
C = (rut//100%10)*4
D = (rut//1000%10)*5
E = (rut//10000%10)*6
F = (rut//100000%10)*7
G = (rut//1000000%10)*2
H = (rut//10000000%10)*3
r= A+B+C+D+E+F+G+H
r1=r/11
r2=r-(11*int(r1))
r3=11-r2
if (r3 == 11):
    print("dv=0")
elif (r3 == 10):
    print("dv=k")
else:
    print("dv=",r3)    