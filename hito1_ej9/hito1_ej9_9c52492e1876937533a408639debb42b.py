def solucion(a,b,c,d,e,f):
    D= a*e - b*d
    
    if D!= 0:
        x=(c*d - b*e)/D
        y=(a*d - c*f)/D
        
        return x, y
    else:
        return None,None
    
    
print("Ingrese un numero para a, b, c,d, e, f ")
a, b, c, d, e, f = map(float, input().split())

print((solucion(a,b,c,d,e,f))