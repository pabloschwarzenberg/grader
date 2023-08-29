#Cálculo del dígito verificador de un rut
rut= int(input("Hola. Para calcular el dígito verifcador de su rut, ingrese su rut, sin dígito verficador, sin puntos ni guión: "))
while not 1000000<=rut<=99999999:
    print("Se equivocó en ingresar rut. Inténtelo de nuevo.")
    rut=int(input("Ingrese rut sin puntos ni guión, y sin dígito verificador: "))
a=rut//10000000
A=a*10
b=(rut//1000000)-A
B=b*10
c=(rut//100000)-(A*10)-B
C=c*10
d=(rut//10000)-(A*100)-(B*10)-C
D=d*10
e=(rut//1000)-(A*1000)-(B*100)-(C*10)-D
E=e*10
f=(rut//100)-(A*10000)-(B*1000)-(C*100)-(D*10)-E
F=f*10
g=(rut//10)-(A*100000)-(B*10000)-(C*1000)-(D*100)-(E*10)-F
G=g*10
h=rut-(A*1000000)-(B*100000)-(C*10000)-(D*1000)-(E*100)-(F*10)-G
m1=h*2
m2=g*3
m3=f*4
m4=e*5
m5=d*6
m6=c*7
m7=b*2
m8=a*3
suma=m1+m2+m3+m4+m5+m6+m7+m8
resto=suma%11
dv=11-resto
if dv==10:
    print("dv=k")
elif dv<10:
    print("dv=", dv)
elif dv==11:
    print("dv=0")