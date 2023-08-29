#Cálculo del dígito verificador de un rut
print("calculemos el digito verificador")
rut = int(input("ingrese su rut sin puntos ni digito verificador: "))
A = (rut//10000000)
B = (rut//1000000) % 10
C = (rut//100000) % 10
D = (rut//10000) % 10
E = (rut//1000) % 10
F = (rut//100) % 10
G = (rut//10) % 10
H = (rut//1) % 10
A1 = H * 2
B1 = G * 3
C1 = F * 4
D1 = E * 5
E1 = D * 6
F1 = C * 7
G1 = B * 2
H1 = A * 3
x = (A1+B1+C1+D1+E1+F1+G1+H1)
y = x % 11
digito = 11 - y
if digito == 11 :
    print("el digito verificador es: 0")
else:
    if digito == 10:
        print("el digito verificador es: K")
    else:
        print("el digito verificador es: ", digito)