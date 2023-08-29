#Conversión de Decimal a Binario
num = int(input("Ingresa un numero:",))
resultado_int = []
i = 1
while i == 1:
    residuo = num % 2
    resultado_int.insert(0,residuo)
    num = (num//2)
    if (num == 1):
        resultado_int.insert(0,num)
        break
resultado_str = []
for a in resultado_int:
    resultado_str.append(str(a))
resultado = "".join(resultado_str)
print("resultado = {}".format(resultado))