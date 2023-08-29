#Nota final
#Entrada de datos
n = float ()
v1 = float ()
v2 = float ()
v3 = float ()
v4 = float ()
prom = float ()
print("escriba el total de notas a calcular promedio: ")
    if(i == 1):
        print("parcial 1 con ponderacion del 30%: ")
        v1 = float(input())
    if(i == 2):
        print("parcial 2 con ponderacion del 30%: ")
        v2 = float(input())
    if(i == 3): 
        print("parcial 3 con ponderacion del 30%: ")
        v3 = float(input())
    if(i == 4):
        print("parcial 4 con ponderacion del 10%: ")
        v4 = float(input())
    n1 = v1*0.3
    n2 = v2*0.3
    n3 = v3*0.3
    n4 = v4*0.1
    prom = n1+n2+n3+n4
print("notas con porcentaje aplicado")
print("parcial 1: ",n1)
print("parcial 2: ",n2)
print("parcial 3: ",n3)
print("parcial 4: ",n4)
print(n1+n2+n3+n4)