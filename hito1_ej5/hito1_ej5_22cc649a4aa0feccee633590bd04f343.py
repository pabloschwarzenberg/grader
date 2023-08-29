from math import trunc

dv = 0
rut = int(input("Ingresar rut: "))
modulo = [2, 3 ,4 ,5 ,6 ,7]
producto= []
resultado = [int(x) for x in str(rut)]
print("Rut: ", str(resultado))
rut = resultado
resultado.reverse()
print("__________________________________________")

print("Rut: ", resultado)
print("Modulo: ", modulo)


for num1, num2 in zip(rut, modulo):
    producto.append(num1 * num2)

producto.append(rut[6] * modulo[0])

if(len(rut) >7):
    producto.append(rut[7] * modulo[1])

print("Resultado multiplicacion: ", producto)

print("Suma valores Rut: ",sum(producto))


dividir = sum(producto) / 11
dividir = trunc(dividir*1)/1
print("Division: ", dividir)

result2 = sum(producto) - (11 * round(dividir,1))
print("Resto: ", result2)
result3 = 11 - result2
print("Resultado final: ", result3)

if (result3 >= 11):
    dv = 0
    print("dv=",dv)

elif (result3 >= 10 and result3 <= 11):
    dv = str(dv)
    dv = "K"
    print("dv=",dv)

else:
    dv = result3
    print("dv=",dv)