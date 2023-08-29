#Sistema de Ecuaciones

print('indique los coeficientes del sistena de ecuaciones lineales\n')
a = float(input('coeficiente a:'))
b = float(input('coeficiente b:'))
c = float(input('coeficiente c:'))
d = float(input('coeficiente d:'))
e = float(input('coeficiente e:'))
f = float(input('coeficiente f:'))
varx = float(c*e-b*f)/(a*e-b*d)
vary = float(a*f-c*d)/(a*e-b*d)
print ('valor de x:',(round(varx, 1)))
print ('valor de y:',(round(vary, 1)))


 