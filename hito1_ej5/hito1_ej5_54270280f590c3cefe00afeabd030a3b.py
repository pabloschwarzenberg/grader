#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut sin num verificador: "))

r = rut
num1 = r // 10**7
r = r % 10**7
num2 = r // 10**6
r = r % 10**6
num3 = r // 10**5
r = r % 10**5
num4 = r // 10**4
r = r % 10**4
num5 = r // 10**3
r = r % 10**3
num6 = r // 100
r = r % 100
num7 = r // 10
r = r % 10
num8 = r // 1

y1 = num1 * 3
y2 = num2 * 2
y3 = num3 * 7
y4 = num4 * 6
y5 = num5 * 5
y6 = num6 * 4
y7 = num7 * 3
y8 = num8 * 2

suma = y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8

modulo = suma % 11
dv = 11 - modulo

if dv == 11:
    print("dv=0")    
elif dv == 10:
    print("dv=k")
else:
    print("dv=",dv)