#Sistema de Ecuaciones
A=eval(input("#1: "))
B=eval(input("#2: "))
C=eval(input("#3: "))
a=eval(input("#4: "))
b=eval(input("#5: "))
c=eval(input("#6: "))
y=round(((a*-C-A*-c)/(A*b-a*B)),1)
x=round(((c-b*y)/a),1)
print("x="+str(x))
print("y="+str(y))