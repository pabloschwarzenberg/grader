#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese el rut sin el digito verificador: "))
lista=[]
for i in rut:
    lista.append(i)

lista.reverse()
multiplicacion = [2, 3, 4, 5, 6, 7]

total = 0

for j in range(len(lista)):
    total+= int(lista[j]) * multiplicacion[j % 6]

resto = total % 11
verificador = 11 - resto

if verificador == 11:
    verificador = 0
elif verificador == 10:
    verificador = "K"
print("dv =", verificador)
      