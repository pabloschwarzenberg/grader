n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese un numero: "))
n3 = int(input("ingrese un numero: "))
n4 = int(input("ingrese un numero: "))
n5 = int(input("ingrese un numero: "))
n6 = int(input("ingrese un numero: "))

dpy = ((n6*n1)-(n4*n3))/((n1*n5)-(n4*n2))

dpx = (n3-n2*dpy)/n1

dpy = round(dpy,1)
dpx = round(dpx,1)

print("['x=",dpx,", 'y=",dpy,"']")
