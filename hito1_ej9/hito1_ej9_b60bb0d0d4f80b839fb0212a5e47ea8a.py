#Sistema de Ecuaciones
print("ecuacion 1")
X1=int(input("Coeficiente X ecuacion 1:"))
Y1=int(input("Coeficiente  Y ecuacion 1:"))
C1=int(input("Coeficiente  C ecuacion 1:"))
print("ecuacion 2")
X2=int(input("Coeficiente X ecuacion 2:"))
Y2=int(input("Coeficiente  Y ecuacion 2:"))
C2=int(input("Coeficiente  C ecuacion 2:"))
D=int(X1*Y2-Y1*X2)
Dx=int(C1*Y2-Y1*C2)
Dy=int(X1*C2-C1*X2)
Xf=(Dx/D)
Yf=(Dy/D)
print("X=",Xf)
print("Y=",Yf)

