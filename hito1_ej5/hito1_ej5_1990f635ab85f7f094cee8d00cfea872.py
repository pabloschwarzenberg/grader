#Cálculo del dígito verificador de un rut
print("Digito Verificador")
Rut = int(input("Ingrese su Rut sin el digito verificador (sin guion): "))
a = (Rut//10000000) * 3
b = ((Rut//1000000)%10) * 2
c = ((Rut//100000)%10) * 7
d = ((Rut//10000)%10) * 6
e = ((Rut//1000)%10) * 5
f = ((Rut//100)%10) * 4
g = ((Rut//10)%10) * 3
h = ((Rut//1)%10) * 2
Total_Suma = (a + b + c + d + e + f + g + h)
Modulo_Once = Total_Suma//11
Resta_Modulo = Total_Suma - (11 * Modulo_Once)
Resta = 11 - Resta_Modulo
if Resta <= 9:
    print("dv=", Resta)
else:
    if Resta == 11:
        print("dv=", 0)
    else:
        Resta == 10
        print("dv= k")