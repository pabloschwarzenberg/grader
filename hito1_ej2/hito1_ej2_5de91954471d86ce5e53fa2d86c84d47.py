#Contestador de celular
print(" Llamada entrante ")
numtel=int(input("Número de teléfono: "))
hora=int(input("Hora de llamada (FORMATO 24hrs): "))
digitos = int (numtel % 1000)
digitus = int (numtel / 100000)

if hora < 7 and hora > 0 :
    print("CONTESTAR")
elif hora < 14 and hora > 7 and digitos == 909 :
    print("CONTESTAR")
elif hora < 19 and hora > 17 and digitus != 877 :
    print("CONTESTAR")
elif digitus == 877 : 
    print("NO CONTESTAR")
elif hora > 19 and hora < 24:
    print("NO CONTESTAR")
          