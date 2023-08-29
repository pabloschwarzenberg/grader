#Cálculo del dígito verificador de un rut
r = input("ingresa rut")
suma=0
contador=2
for i in range(len(r), 0, -1):
    suma = suma + (int(r[i-1]) * contador)
    contador += 1
    if(contador >= 8):
        contador = 2 

dv=11-suma % 11
if(dv == 11):
    dv=0
elif(dv == 10):
    dv = "K"
print("dv=" + str(dv))
