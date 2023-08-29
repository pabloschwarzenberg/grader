#Nota final
pt = eval(input("ingrese ñla nota de sus tareas: "))
pi = eval(input("ingrese la nota de sus interrogaciones: "))
ne = eval(input("ingrese la nota de sus examenes: "))
pp = eval(input("ingrese la nota de sus presentaciones: "))

formula = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
print(formula)
strformula = str(formula)
print(strformula)
Tformula = formula
strTformula = Tformula
centesima = (strformula[3:4])
print(centesima)
if(int(centesima) >= 6):
    Tformula = formula + 0.1
    strTformula = Tformula
    print(strTformula[0:3])
decima = (strformula[2:3])
print(decima)
if(int(decima) >= 6):
    Tformula = formula + 1
    strTformula = Tformula
    print(strTformula[0:2])
    print("su promedio es: ",strTformula[0:1])
else:
    print("supromedio es: ", strTformula[0:2])