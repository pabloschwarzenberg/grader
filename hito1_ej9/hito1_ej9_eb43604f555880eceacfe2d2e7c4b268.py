print(" programa para resolver un sistema de ecuaciones de la forma Ax+By=C")
A=float(input("ingrese el valor que acompaña a X en la primera ecuacion"))
B=float(input("ingrese el valor que acompaña a Y en la primera ecuacion"))
E=float(input("ingrese el valor sin incognita de la primera ecuacion"))
C=float(input("ingrese el valor que acompaña a X en la segunda ecuacion"))
D=float(input("ingrese el valor que acompaña a Y en la segunda ecuacion"))
F=float(input("ingrese el valor sin incongnita de la segunda ecuacion"))
if A==0:
    if D==0:
        print("la solucion es(",round((F/C),1),round((E/B),1),")")
    else:
        y=(E/B)
        x=((F-(D*y))/C)
        print("la solucion es (",round(x,1),round(y,1),")")
elif C==0:
    if B==0:
        print("la solucion es (",E/A,F/D,")")
    else:
        y=F/D
        x=((E-(B*y))/A)
        print("La solucion es ",round(x,1),round(y,1),")")
elif B==0:
    x=E/A
    y=(((F-(D*x))/C))
    print("la solucion es(",round(x,1),round(y,1),")")
elif D==0:
       x=F/C
       Y=((E-(A*x))/B)
       print("la solucion es (",round(x,1),round(y,1),")")
elif -A/B==-C/D and E/B==F/D:
    print("tiene infinitas soluciones")
elif -A/B==-C/D and E/B!=F/D:
    print("no tiene solucion")
else:
    y=(((C*E)-(F*A))/((B*C)-(D*A)))
    x=(((E-(B*y))/A))
    print("la solucion es (",round(x,1),round(y,1),")")

