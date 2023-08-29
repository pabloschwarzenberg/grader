#Cálculo del dígito verificador de un rut
rut= input("Ingrese rut: ")
largo = len(rut)
suma= 0
serie = "2","3","4","5","6","7"
j= 0
i=int (largo) - 1

while i >= 0:
    multiplicacion = int (rut[i])* (int(serie[j]))
    suma = suma + multiplicacion
    i = i-1
    j= j+1
    if j ==6:
        j=0
        

modulo = suma %11
division = suma / 11
resta = 11 - modulo

if resta == 11 :
    dv= 0
elif resta == 10:
    dv = "k"
else:
    dv = resta

print ("dv=",dv)