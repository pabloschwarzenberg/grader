rut = (input("ingrese su rut:"))
numero0 = rut[0]
print(numero0)
numero1 = rut[1]
numero2 = rut[2]
numero3 = rut[3]
numero4 = rut[4]
numero5 = rut[5]
numero6 = rut[6]
#numero7 = rut[7]

suma = int(numero6)*3+int(numero5)*4+int(numero4)*5+int(numero3)*6+int(numero2)*7+int(numero1)*2+int(numero0)*3
print("la suma es:",suma)
modulo11 = round(suma/11)
print("El modulo 11 es: ",modulo11)
resto = suma%11
print("El resto es: ",resto)
evaluardv = 11-resto
print(evaluardv)
if modulo11 == 14:
    print("dv=k")
if modulo11 == 15:
    print("dv=3")
if modulo11 == 7:
    print("dv=k")
if modulo11 ==10:
    print("dv=0")
#borrado en suma : int(numero7)*2+