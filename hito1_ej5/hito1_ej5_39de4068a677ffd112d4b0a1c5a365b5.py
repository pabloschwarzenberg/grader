#Cálculo del dígito verificador de un rut
rut=int(input("ingresa tu rut sin digito verificador: "))
aux=0
h=2

while rut>0:
    aux+=((rut%10)*h)
    rut=rut//10

    if h==7:
        h=2
    else:
        h+=1

print(aux)
resto=aux%11

digito=11-resto
if digito==10:
    digito="k"
elif digito==11:
    digito=0

print("dv=",digito)