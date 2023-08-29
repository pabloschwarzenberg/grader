#Cálculo del dígito verificador de un rut
rut = input("ingrese rut: ")
lista = []
for digito in rut:
    lista.append(int(digito))
    
lista.reverse()
i = 2
suma = 0
for numero in lista:
    if i <= 7:
        suma += numero * i
        i +=1 
    else:
        i -= 6
        suma += numero * i
        i += 1

RF = 11 - (suma%11)
if RF == 11:
    DV = 0
elif RF == 10:
    DV = "K"
else:
    DV = RF
    
print("dv=" + str(DV))      