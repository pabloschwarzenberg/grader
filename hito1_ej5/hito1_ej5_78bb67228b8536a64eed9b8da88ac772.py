#Cálculo del dígito verificador de un rut
rut = input("")
suma = 0
contador = 2
for i in range(len(rut),  0, -1):
    suma = suma + (int(rut[i-1]) * contador)
    contador += 1
    if(contador >= 8):
        contador = 2    
dv = 11 - suma % 11
if(dv == 11):
    dv = 0
elif(dv == 10):
    dv = "k"
print("dv=" + str(dv))