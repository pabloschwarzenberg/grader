rut = int(input("Ingrese el rut:"))
a = (rut//10000000)*3
b = ((rut//1000000)%10)*2
c = ((rut//100000)%10)*7
d = ((rut//10000)%10)*6
e = ((rut//1000)%10)*5
f = ((rut//100)%10)*4
g = ((rut//10)%10)*3
h = ((rut//1)%10)*2
suma = a+b+c+d+e+f+g+h
suma_6= b+c+d+e+f+g+h
div = suma//11
div_6 = suma_6//11
resto = suma-(11*div)
resto_6 = suma_6-(11*div_6)
dv= 11- resto
dv_6 = 11-resto_6

if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=K")
elif dv_6 == 11:
    print("dv=0")
elif dv_6==10:
    print("dv=K")
else:
    print("dv=",dv)
    print("dv=",dv_6)
