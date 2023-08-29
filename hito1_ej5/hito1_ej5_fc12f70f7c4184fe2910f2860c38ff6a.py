#Cálculo del dígito verificador de un rut
rut=input("ingrese su rut sin punto: ")
n1=rut[0:1]
print(n1)
n2=rut[1:2]
print(n2)
n3=rut[2:3]
print(n3)
n4=rut[3:4]
print(n4)
n5=rut[4:5]
print(n5)
n6=rut[5:6]
print(n6)
n7=rut[6:7]
print(n7)
n8=rut[7:8]
print(n8)
contador=int(1)
control=int(10)
while control<=int(rut):
    contador=contador+1
    control=control*10
if int(contador)==8:
    num= int(n8)*2 + int(n7)*3 + int(n6)*4 + int(n5)*5 + int(n4)*6 + int(n3)*7 + int(n2)*2 + int(n1)*3
    digito= int(num)%11
    print("<",digito,"<")
    ver=11-int(digito)
    if ver==11:
        print("dv=0")
    elif ver==10:
        print("dv=k")
    else:
        print("dv=",ver)
else:
    num= int(n7)*2 + int(n6)*3 + int(n5)*4 + int(n4)*5 + int(n3)*6 + int(n2)*7 + int(n1)*2
    digito= int(num)%11
    print("<",digito,"<")
    ver=11-int(digito)
    if ver==11:
        print("dv=0")
    elif ver==10:
        print("dv=k")
    else:
        print("dv=",ver)