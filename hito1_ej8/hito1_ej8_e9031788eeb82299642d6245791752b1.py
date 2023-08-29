#Descomponer un número
import math
x = float(input("ingrese numero de 4 cifras: "))
mil = x/1000
m = math.trunc(mil)
cien = (x/100)-(m*10)
c = math.trunc(cien)
decena = (x/10)-((m*100)+(c*10))
d = math.trunc(decena)
unidad = (x-((m*1000)+(c*100)+(d*10)))
u = math.trunc(unidad)
if x > 1000:
    print(m,"M+", c,"C+", d,"D+", u,"U")
else:
    if 100 < x <= 999:
        print(c,"C+", d,"D+", u,"U")
    else:
        if 10 < x <= 99:
            print(d,"D+", u,"U")
        else:
            print(u,"U")    