#Descomponer un número
n=(input("Ingresa tu rut sin digito verificador"))
m=int(n)
largo=len(n)
if (int(largo))==8:
    suma=((int(n[7]))*2)+((int(n[6]))*3)+(int((n[5]))*4)+((int(n[4]))*5)+((int(n[3]))*6)+((int(n[2]))*7)+((int(n[1]))*2)+((int(n[0]))*3)
else:
    suma=((int(n[6]))*2)+((int(n[5]))*3)+((int(n[4]))*4)+((int(n[3]))*5)+((int(n[2]))*6)+((int(n[1]))*7)+((int(n[0]))*2)

resto=suma//11
caca=suma-(resto*11)

digito=11-caca

if digito<=9:
    print("dv=",digito)
else:
    if digito==10:
        print("dv=","k")
    elif digito==11:
        print("dv=","0")