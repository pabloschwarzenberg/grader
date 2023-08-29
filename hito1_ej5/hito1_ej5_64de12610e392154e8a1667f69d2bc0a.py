#Cálculo del dígito verificador de un rut
A = int(input("Ingrese el primer digito del RUT: "))
B = int(input("Ingrese el segundo digito del RUT: "))
C = int(input("Ingrese el tercer digito del RUT: "))
D = int(input("Ingrese el cuarto digito del RUT: "))
E = int(input("Ingrese el quinto digito del RUT: "))
F = int(input("Ingrese el sexto digito del RUT: "))
G = int(input("Ingrese el septimo digito del RUT: "))
H = int(input("Ingrese el octavo digito del RUT: "))

#Procesamiento
resultante = (H*2) + (G*3) + (F*4) + (E*5) + (D*6) + (C*7) + (B*2) + (A*3)
resultante_2 = (resultante // 11)
resultante_3 = resultante - (11*resultante_2)
resultante_4 = 11 - resultante_3
if resultante_4 == 11:
    print("dv = 0")
elif resultante_4 == 10:
    print("dv = K")
else:
    print("dv =", resultante_4)