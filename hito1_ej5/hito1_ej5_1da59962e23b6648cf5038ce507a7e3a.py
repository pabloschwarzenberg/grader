#Cálculo del dígito verificador de un rut
rut= int(input("ingrese el numero :"))
num8 = rut % 10
num7 = int((rut % 100) /10)
num6 = int((rut % 1000) /100)
num5 = int((rut % 10000) /1000)
num4 = int((rut % 100000) /10000)
num3 = int((rut % 1000000) /100000)
num2 = int((rut % 10000000) /1000000)
num1 = int((rut % 100000000) /10000000)
paso1=num8*2+num7*3+num6*4+num5*5+num4*6+num3*7+num2*2+num1*3
paso2=paso1/11
x=int(paso2)
paso3=paso1-(11*x)
paso4=11-paso3
if paso4==11:
    print("dv=0")
elif paso4==10:
    print("dv=K")
else:
    print("dv=",paso4)      