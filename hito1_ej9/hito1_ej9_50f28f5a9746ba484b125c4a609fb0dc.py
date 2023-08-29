def resolver_sistema(n1, n2, n3, n4, n5, n6):
    #n1X*n2Y=n3   n4X*n5Y=n6
    d1=(n1*n5)
    d2=(n2*n4)
    div= d1-d2
    if div==0:
        print("El sistema no tiene solución única.")
    else:
        valx =((n3*n5)-(n2*n6))//div #26-27
        valy =((n1*n6)-(n3*n4))//div #18-13
        print("X=" ,valx)
        print("y=" ,valy) 

n1=float(input("Ingrese numero: "))
n2=float(input("Ingrese numero: "))
n3=float(input("Ingrese numero: "))
n4=float(input("Ingrese numero: "))
n5=float(input("Ingrese numero: "))
n6=float(input("Ingrese numero: "))
resolver_sistema(n1, n2, n3, n4, n5, n6)