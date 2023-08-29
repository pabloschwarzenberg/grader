PT = float(input("Inserte la nota de tareas: "))
PI = float(input("Inserte la nota de las interrogaciones: "))
NE = float(input("Inserte la nota de los examenes: "))
PP = float(input("Inserte la nota de las presentaciones: "))
def cal(x):
    r=x*0.3
    return r
def cal2(x):
    r=x*0.1
    return r
print(str(round(cal(PT)+cal(PI)+cal(NE)+cal2(PP),1)))