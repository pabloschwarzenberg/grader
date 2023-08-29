#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su RUT, sin puntos ni guión: "))
ocho = (rut % 10)
siete=(rut % 100)
siete=int(siete / 10)
seis=(rut % 1000)
seis=int(seis / 100)
cinco=(rut % 10000)
cinco=int(cinco / 1000)
cuatro=(rut % 100000)
cuatro=int(cuatro / 10000)
tres=(rut % 1000000)
tres=int(tres / 100000)
dos=(rut % 10000000)
dos=int(dos / 1000000)
uno=(rut % 100000000)
uno=int(uno / 10000000)
#print(uno,dos,".",tres,cuatro,cinco,".",seis,siete,ocho)
#Multiplicando por 2, 3, 4, 5, 6, y 7
suma=ocho*2+siete*3+seis*4+cinco*5+cuatro*6+tres*7+dos*2+uno*3
division=int(suma/11)
parteentera=int(suma-division*11)
digito=int(11-parteentera)
if digito==11:
  print("dv=0")
elif digito==10:
  print("dv=K")
else:
  print("dv=",digito)