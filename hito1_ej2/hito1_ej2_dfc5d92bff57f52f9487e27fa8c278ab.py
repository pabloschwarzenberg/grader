#Contestador de celular

n = int(input("ingrese un numero con 8 cifras : "))
hr = int(input("ingrese la hora de llamada (dos cifras de 0 a 23 horas): "))

inicia = n//100000
termina = n % 1000
contesta = True

if(hr>=0 and hr<=7):
    print("CONTESTAR")

if(hr>=8 and hr<=14):
    if(termina == 909):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if(hr>14 and hr<17):
    print("NO CONTESTAR")

if(hr>=17 and hr<=19):
    if(inicia == 877):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")


if(hr>=19 and hr<=23):
    print("NO CONTESTAR")