x = str(input("Ingrese un numero (Hasta 4 digitos)"))

h=0
final = ""
uni = ""
dec = ""
cen = ""
mil = ""



if len(x) >=4:
    mil = x[-4] + "M"
if len(x) >= 3:
    cen = x[-3] + "C"
if len(x) >= 2:
    dec = x[-2] + "D"
if len(x) >= 1:
    uni = x[-1] + "U"

desc = [mil,cen,dec,uni]

for w in desc:
    final += w
    if w != "" :
        final += "+"
        
print(final[0:len(final)-1])
    