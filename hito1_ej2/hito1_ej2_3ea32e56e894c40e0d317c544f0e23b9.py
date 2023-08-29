#Contestador de celular
n_telefono=float(input("ingrese el numero telefonico: "))
h_llamada=float(input("ingrese la hora de la llamada: "))
ultimos_3=n_telefono//1%1000
primeros_3=n_telefono//100000%1000

if 0<= h_llamada <=7:
    contestar=1

if 8<= h_llamada <=14:
    if ultimos_3==909:
        contestar=1
    else:
        contestar=0


if 17<= h_llamada <=19:
    if primeros_3==877:
        contestar=0
    else:
        contestar=1

if h_llamada>19:
    contestar=0
print(contestar)
if contestar==1:
    print("CONTESTAR")
else:
    contestar==0
    print("NO CONTESTAR")