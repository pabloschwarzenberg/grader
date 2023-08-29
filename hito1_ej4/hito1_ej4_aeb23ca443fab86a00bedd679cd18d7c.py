numero=0
modulo=[]

numero=int(input("ingrese numero:"))

while numero!=0:
    residuo = (numero % 2)
    numero = (numero // 2)
    modulo.append(residuo)

modulo=modulo[::-1]
print(f"el numero binario es: {modulo}")