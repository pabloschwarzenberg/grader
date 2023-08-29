telefono = int(input("Ingrese numero telefonico: "))
termina = telefono%1000
comienza = telefono//100000
hora = int(input("Ingrese hora de la llamada: "))
if 0 <= hora <= 7:
    print("Resultado: CONTESTAR")
elif 8<= hora <=14 and termina == 909:
    print("Resultado: CONTESTAR")    
elif 17 <= hora <= 19 and comienza != 877:
    print("Resultado: CONTESTAR")    
else:
    print("Resultado: NO CONTESTAR")
