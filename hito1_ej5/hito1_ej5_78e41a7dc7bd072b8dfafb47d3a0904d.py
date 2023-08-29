#Cálculo del dígito verificador de un rut
rut=int(input("Por favor ingrese el RUT del cual quiere saber el digito verificador (sin puntos): "))
verificador=""

# Descomponer el rut por sus unidades y multiplicar por la serie de derecha a izquierda
# Serie: 2, 3, 4, 5, 6, y 7
a=(rut//10000000) * 3
b=((rut//1000000)%10) * 2
c=((rut//100000)%10) * 7
d=((rut//10000)%10) * 6
e=((rut//1000)%10) * 5
f=((rut//100)%10) * 4
g=((rut//10)%10) * 3
h=((rut//1)%10) * 2
suma=(a+b+c+d+e+f+g+h)

# Sacar resto de la suma
resto1=(suma//11)
resto2=(suma-(resto1*11))
resto_final=11-resto2

# Comparar resto para sacar verificador
if (resto_final == 11):
	verificador="0"
elif (resto_final == 10):
	verificador="K"
else:
	verificador=str(resto_final)

print("dv=", verificador)