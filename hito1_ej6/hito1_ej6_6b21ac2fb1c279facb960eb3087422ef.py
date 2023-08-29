numero1 = int(input("Ingresa un numero"))
numero2 = int(input("Ingresa un numero"))
numero3 = int(input("Ingresa un numero"))
if numero1 > numero2 and numero1 > numero3:
  nunmayor = numero1
elif numero2 > numero1 and numero2 > numero3:
  nunmayor = numero2
else:
  nunmayor = numero3

if numero1 < numero2 and numero1 < numero3:
  nunmenor = numero1
elif numero2 < numero1 and numero2 < numero3:
  nunmenor = numero2
else:
  nunmenor = numero3

if nunmayor == numero1 and nunmenor == numero2:
     nunmedio = numero3
elif nunmayor == numero2 and nunmenor == numero1:
        nunmedio = numero3
elif nunmayor == numero3 and nunmenor == numero1:
        nunmedio = numero2
elif nunmayor == numero1 and nunmenor == numero3:
        nunmedio = numero2
else:
    nunmedio = numero1

print(str(nunmenor) +","+ str(nunmedio) +","+ str(nunmayor))