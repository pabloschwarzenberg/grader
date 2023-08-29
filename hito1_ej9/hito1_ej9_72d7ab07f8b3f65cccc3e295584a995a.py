#Sistema de Ecuaciones
print("ingrese los valores para a: ")
print("ingrese los valores para b: ")
print("ingrese los valores para c: ")
print("ingrese los valores para d: ")
print("ingrese los valores para e: ")
print("ingrese los valores para f: ")
a,b,c,d,e,f =map(float,input().split())

def solucion_sistema_ecuaciones(a,b,c,d,e,f):
    determinante = a*e-b*d
    
    if determinante !=0:
        x= (c*e-b*f)/determinante
        y=(a*f-c*d)/determinante
        
        return x,y
    else:
        return None,None
    
print(solucion_sistema_ecuaciones(a, b, c, d, e, f)) 