
#Cálculo del dígito verificador de un rut
multiplicadores=[2,3,4,5,6,7,2,3]
lista_rut=[]
producto=[]
b = []

rut = int(input("Ingrese su rut sin digito verificador: "))
lista_rut = [int(a) for a in str(rut)]
b = reversed(lista_rut)
producto = [x*y for x,y in zip(b,multiplicadores)]

suma = sum(producto)

resto = suma/11
multiplicacion = suma - (11 * int(resto))
digito_ver = 11 - multiplicacion
print(lista_rut)
print(b)
print(multiplicadores)
print(producto)
print(suma)
print(resto)
print(multiplicacion)
if digito_ver==11:
    print("dv=0")
elif digito_ver==10:
    print("dv=k")
else:
    print("dv=",digito_ver)
