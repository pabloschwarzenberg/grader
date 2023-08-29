n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese un numero: "))
n3 = int(input("ingrese un numero: "))
n4 = int(input("ingrese un numero: "))
n5 = int(input("ingrese un numero: "))
n6 = int(input("ingrese un numero: "))

dpy = ((n6n1)-(n4n3))/((n1n5)-(n4n2))

dpx = (n3-n2*dpy)/n1

dpy = round(dpy,1)
dpx = round(dpx,1)

print("['x=",dpx,", 'y=",dpy,"']")