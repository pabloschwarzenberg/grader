#Cálculo del dígito verificador de un rut
rut = input("Ingrese el RUT sin dígito verificador: ")
funcionando = True
numbers = len(rut)
zero = 0

while funcionando:
        for i in range(2, 8):
            if numbers != 0:
                zero += int(rut[numbers-1]) * i
                numbers -= 1

            else:
                funcionando = False
        
resto = zero % 11
digito = 11 - resto

if digito == 11:
    print("dv=0")
elif digito == 10:
    print("dv=k")
else:
    print("dv=",digito)