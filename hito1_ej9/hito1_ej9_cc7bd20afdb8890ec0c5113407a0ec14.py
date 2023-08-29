a=int(input("ingrese el coeficiente de la x de la primera ecuación:"))
b=int(input("ingrese el coeficiente de la y de la primera ecuación:"))
c=int(input("ingrese el resultado de Ax+By en la primera ecuación:"))
d=int(input("ingrese el coeficiente de la x en la segunda ecuación:"))
e=int(input("ingrese el coeficiente de la y en la segunda ecuación:"))
f=int(input("ingrese el resultado de Cx+By en la segunda ecuación:"))

if (a!=0 and d!=0):
    y=float(round(((a*f-d*c)/(a*e-b*d)),1))
    x=round(((c-y*b)/a),1)
    print("x="+str(x))
    print ("y="+str(y))