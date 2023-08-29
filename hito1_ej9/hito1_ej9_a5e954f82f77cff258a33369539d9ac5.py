#Sistema de Ecuaciones
a1=eval(input('Ingrese el primer x: '))
b1=eval(input('Ingrese la primera y: '))
c1=eval(input('Ingrese el primer valor independiente: '))
a2=eval(input('Ingrese el segundo x: '))
b2=eval(input('Ingrese la segunda y: '))
c2=eval(input('Ingrese el segundo valor independiente: '))
listaA=['x=','y=']

def SisEcua(a1,b1,c1,a2,b2,c2):
  h=a1*b2-b1*a2
  if h!=0:
    x=(c1*b2-b1*c2)/h
    y=(a1*c2-c1*a2)/h
    return x,y
    
resultado=(SisEcua(a1,b1,c1,a2,b2,c2))
listaA[0]+=str(resultado[0])
listaA[1]+=str(resultado[1])
print(listaA)