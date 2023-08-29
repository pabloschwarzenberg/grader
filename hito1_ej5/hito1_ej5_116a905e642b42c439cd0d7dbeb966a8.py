#Cálculo del dígito verificador de un rut
rut=str(input("Ingrese su rut sin puntos ni digito verificador: "))
lista=[]
suma=0
n=2

for i in rut:
    lista.append(i)

lista.reverse()

for i in lista:
    s=int(i)*n
    suma=suma+s
    n=n+1
    if n==8:
        n=2

parte_entera=suma//11

resto=suma-(11*parte_entera)

final=11-resto

if final==11:
    print("dv=0")

elif final==10:
    print("dv=K")
else:
    print("dv=",final)