#Sistema de Ecuaciones
coef1=input("Coeficiente 1: ")
coef1=float(coef1)

coef2=input("Coeficiente 2: ")
coef2=float(coef2)

coef3=input("Coeficiente 3: ")
coef3=float(coef3)

coef4=input("Coeficiente 4: ")
coef4=float(coef4)

coef5=input("Coeficiente 5: ")
coef5=float(coef5)

coef6=input("Coeficiente 6: ")
coef6=float(coef6)

y=(coef3-(coef1*coef6/coef4))/(coef2-(coef1*coef5/coef4))
x=(coef6-(coef5*y))/coef4

print("y=", y)
print("x=", x)
