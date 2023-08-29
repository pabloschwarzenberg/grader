#Cálculo del dígito verificador de un rut
rut = input("Ingrese el rut sin digito verificador: ")
x = len(rut)
val = 0
serie = "765432"
y = len(serie)
while x > 0 :
    val = int(rut[x-1])*int(serie[y-1]) + val
    x = x - 1
    y = y - 1 
a =  (val // 11)
dv = 11 - (val - (11* a))
if(dv == 11):
    print("dv=", 0)
if(dv == 10):
    print("dv=", "K")
print("dv=", dv)