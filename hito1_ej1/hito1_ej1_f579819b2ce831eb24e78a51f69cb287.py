#Nota final
a = input("Nota tareas:")
b = input("Nota interrogaciones:")
c = input("Nota examen:")
d = input("Nota presentacion:")
T = float(a)
I = float(b)
N = float(c)
P = float(d)
def f(T,I,N,P):
    return T*3/10+I*3/10+N*3/10+P*1/10
print(round(f(T,I,N,P),1))