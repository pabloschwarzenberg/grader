#Aprobación de créditos

ingreso = int(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijo = int(input("Ingrese cuantos hijos tiene: "))
años = int(input("Ingrese los años que ha pertenecido al banco: "))

estado = (input("'S': soltero, 'C': casado\nIngrese su estado civil: "))

vivienda = (input("'U': urbano, 'R': rural\nIngrese donde vive actualmente: "))

edad = 2021 - nacimiento

if (años > 10) and (hijo >= 2):
    print("\nAPROBADO")
    
elif ((estado == "C") and (hijo > 3)) and (45 <= edad <= 55):
    print("\nAPROBADO")
    
elif (ingreso > 2500000) and (estado == "S") and (vivienda == "U"):
    print("\nAPROBADO")
    
elif (ingreso > 3500000) and (años > 5):
    print("\nAPROBADO")
    
elif (vivienda == "R") and (estado == "C") and (hijo < 2):
    print("\nAPROBADO")
    
else:
    print("\nRECHAZADO")