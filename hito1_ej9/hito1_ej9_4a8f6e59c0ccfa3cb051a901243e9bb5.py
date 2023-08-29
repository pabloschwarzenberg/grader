#Sistema de Ecuaciones
N1 = int(input("ingrese un numero: "))
N2 = int(input("ingrese un numero: "))
N3 = int(input("ingrese un numero: "))
N4 = int(input("ingrese un numero: "))
N5 = int(input("ingrese un numero: "))
N6 = int(input("ingrese un numero: "))

dpy = ((N6*N1)-(N4*N3))/((N1*N5)-(N4*N2))

dpx = (N3-N2*dpy)/N1

dpy = round(dpy,1)
dpx = round(dpx,1)

print("['x=",dpx,", 'y=",dpy,"']")