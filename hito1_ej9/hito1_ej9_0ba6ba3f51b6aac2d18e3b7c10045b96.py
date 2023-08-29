#Sistema de Ecuaciones
a=int(input('1ra variable X ec1:'))
b=int(input('2da variable Y ec1:'))
c=int(input('resultado ecuacion 1:'))
d=int(input('1ra variable X ec2:'))
e=int(input('2da variable Y ec2:'))
f=int(input('resultado ecuacion 2:'))
E1=(str(a)+"x+")+(str(b)+"y=")+(str(c))
E2=(str(d)+"x+")+(str(e)+"y=")+(str(f))
#print("-----")
#print(E1)
#print(E2)
#print("-----")
x=round((f-e*c/b)/(d-a*e/b),1) #valor en x
y=round(((c-a*x)/b),1)         #valor en y
print('x=',x)
print('y=',y)

      