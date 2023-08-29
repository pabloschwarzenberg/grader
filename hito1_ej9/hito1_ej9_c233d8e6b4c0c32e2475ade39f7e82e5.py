#Sistema de Ecuaciones
print('Sistema de ecuaciones')
x1= float( input (" Ingesa x de la primera ecuación : "))
y1= float( input (" Ingesa y de la primera ecuación : "))
a= float( input (" Ingesa valor de la derecha de la primera ecuación : "))
x2= float( input (" Ingesa x de la segunda ecuación : "))
y2= float( input (" Ingesa y de la segunda ecuación : "))
b= float( input (" Ingesa valor de la derecha de la segunda ecuación : "))
det= x1*y2-x2*y1
detx= a*y2-y1*b
dety= x1*b-a*x2
x=(detx/det)
y=(dety/det)
print('x=',x)
print('y=',y)



