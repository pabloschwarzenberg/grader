#Entradas

n = int(input("Ingrese un numero: "))

# Procesamiento

millares=int(n/1000)
centenas=int((n-(millares*1000))/100)
decenas=int((n- (millares*1000 + centenas*100))/10)
unidades=int(n-(millares*1000 + centenas*100 + decenas*10 ))


if millares >= 0:
    x = millares

if centenas >= 0:
    x1 = centenas

if decenas >= 0:
    x2 = decenas

if unidades == 0 or unidades > 0:
    x3 = unidades

                
# Salidas

print(x , "M", "+", x1, "C", "+", x2 , "D", "+", x3, "U")





