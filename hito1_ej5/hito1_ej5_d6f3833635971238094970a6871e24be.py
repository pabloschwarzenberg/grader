#Cálculo del dígito verificador de un rut
RUT = int(input("Ingresar rut sin dígito , sin puntos ni quión verificador :"))
num1 = 2
num2 = 3
num3 = 4 
num4 = 5
num5 = 6
num6 = 7
num7 = (RUT // 10000000) * (num2)
num8 = ((RUT // 1000000) %10) * (num1)
num9 = ((RUT // 100000) %10) * (num6)
num10 = ((RUT // 10000) %10) * (num5)
num11 = ((RUT // 1000) %10) * (num4)
num12 = ((RUT // 100) %10) * (num3)
num13 = ((RUT // 10) %10) * (num2)
num14 = ((RUT // 1) % 10) * (num1)
num15 = (num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14)
num16 = 11
num17 = num15 // num16
num18 = num15 - (num16 * num17)
resultado = num16 - num18
if resultado == 11:
    print("El dígito verificador es dv=0")
else:
    if resultado == 10:
        print("El dígito verificador es dv=k")
    else:
        print("El dígito verificador es dv=",resultado)
        

