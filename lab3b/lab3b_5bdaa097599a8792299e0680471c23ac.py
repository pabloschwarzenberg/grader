#calculadora
Max=0
cantidad=0
suma=0
N=0
while N!=-1 :
    print("Ingrese el numero: ")
    N=int(input())
    
    
    if(N>Max):
        Max=N
    if N!=-1:
        cantidad=cantidad+1
        suma=N+suma
if(cantidad!=0):
    print('cantidad=',cantidad)
    print('suma=',suma)     
    print("maximo=",Max)
else:
    print('cantidad=',cantidad)
    print('suma=',suma)     
    print("maximo=nd")
