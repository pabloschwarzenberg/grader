#Cálculo del dígito verificador de un rut
rut = input("Ingrese el rut: ")
acum = 0
largo = len(rut)
contador=1

for i in range(largo-1,-1,-1):
    contador =  contador + 1
    acum = acum + int(rut[i])*contador
    print(int(rut[i])*contador)
    if contador==7:
        contador = 1

modulo = acum %11
digiver = 11-modulo

if digiver ==11:
    digiver = 0
elif digiver ==10:
    digiver = "k" 
    
print("dv =", digiver)  