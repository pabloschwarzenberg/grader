#contestador de celular
print("llamada entrante")
numtel=int(input("numero telefonico: "))
hora=int(input("hora de llamada (formato 24 hrs): "))
digitos = int (numtel % 1000)
digitus = int (numtel / 100000)

if hora < 7 and hora > 0:
    print("contestar")
elif hora < 14 and hora > 7 and digitos == 909 :
    print("contestar")
elif hora < 19 and hora > 17  and digitus != 877 :
    print("contestar")
elif digitus == 877:
    print("no contestar")
elif hora > 19 and hora < 24 :
    print("no contestar")