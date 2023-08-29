#Descomponer un número
print("Descomposición numérica")
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

if numero>9999:
    print("Debe ingresar un número de hasta 4 dígitos, por favor ingréselo nuevamente...")
elif 1000 <= numero <= 9999:
    umil = numero / 1000
    tmp = numero % 1000
    centenas = tmp / 100
    tmp = tmp % 100
    decenas = tmp / 10
    unidades = tmp % 10
    print("Su descomposición numérica es ""%iM" %umil, "+", "%iC" %centenas, "+", "%iD" % decenas, "+", "%iU" %unidades )
elif 100 <= numero <=999:
    centenas = numero / 100
    tmp = numero % 100
    decenas = tmp / 10
    unidades = tmp % 10
    print("Su descomposición numérica es ""%iC" % centenas, "+", "%iD" % decenas, "+", "%iU" % unidades)
elif 10 <= numero <=99:
    decenas = numero / 10
    unidades = numero % 10
    print("Su descomposición numérica es ""%iD" % decenas, "+", "%iU" % unidades)
else:
    1 <= numero <=9
    unidades = numero % 10
    print("Su descomposición numérica es ""%iU" % unidades)
      