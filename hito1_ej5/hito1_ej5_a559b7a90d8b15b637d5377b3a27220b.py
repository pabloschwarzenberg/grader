#Cálculo del dígito verificador dor

Rut = int(input("Imgrese 8 números: "))
n1 = (Rut%100000000//10**7)
n2 = (Rut%10000000//10**6)
n3 = (Rut%1000000//10**5)
n4 = (Rut%100000//10**4)
n5 = (Rut%10000//10**3)
n6 = (Rut%1000//10**2)
n7 = (Rut%100//10)
n8 = (Rut%10)
suma_de_productos = (n1*3+n2*2+n3*7+n4*6+n5*5+n6*4+n7*3+n8*2)
Parte_entera = (suma_de_productos//11)
Resto = (suma_de_productos-(11*Parte_entera))
Resultado_final = (11-Resto)

#Condiciones
if Resultado_final == 11:
    print("dv = 0")
elif Resultado_final == 10:
    print("dv = K")
else:
    print("dv = " + str(Resultado_final))