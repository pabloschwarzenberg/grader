rut=int(input("ingrese su rut sin el digito verificador: "))
rut2=str(rut)
num1=int(rut2[7])
num2=int(rut2[6])
num3=int(rut2[5])
num4=int(rut2[4])
num5=int(rut2[3])
num6=int(rut2[2])
num7=int(rut2[1])
num8=int(rut2[0])
operacion=(num1*2)+(num2*3)+(num3*4)+(num4*5)+(num5*6)+(num6*7)+(num7*2)+(num8*3)
operacion2=operacion//11
operacion3=operacion-(11*operacion2)
operacion4=11-operacion3
if(operacion4==11):
    print("dv=0")
elif (operacion4==10):
    print("dv=k")
elif operacion4<10:
    print("dv=", operacion4)