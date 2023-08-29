#Contestador de celular

#Entrada

numeroValido = numero = int(input("Ingrese el número telefónico: "))
horaValida = hora = int(input("Ingrese la hora de llamada: "))

#Restricciones

if numero<0 or numero>99999999 :
    print("Número inválido.")
elif numero>0 or numero==0 or numero<99999999 or numero==99999999 :
    numero == numeroValido
elif hora>23 or hora<0 :
    print("Hora inválida.")
elif hora>=0 and hora<=23 :
    hora == horaValida

#Evaluación

if horaValida>=0 and horaValida<=7 :
    print("CONTESTAR")

elif horaValida>7 and horaValida<=14 and numeroValido%1000==909 :
    print("CONTESTAR")
elif numeroValido%1000!=909 :
    print("NO CONTESTAR")

elif horaValida>=17 and horaValida<=19 :
    print("CONTESTAR")
elif numeroValido//100000 :
    print("NO CONTESTAR")

elif horaValida>19 and horaValida<0 :
    print("NO CONTESTAR")
