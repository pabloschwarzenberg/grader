#programa para contestar el telefono
telefono=int(input("Ingrese un numero telefonico: "))
hora=int(input("Ingrese la hora de la llamada: "))
#Reglas


#Si el telfeono termina en 877 o 909
n1=telefono%1000
n2=telefono//100000

#Desarrollo

#Si la llamada es entre 0 y 7 
if hora <= 7:
    print('CONTESTAR')
    
#Si ocurre antes de las 14hrs o si termina en el numero en 909
if hora <= 14 and n1 != 909:
    print("NO CONTESTAR")
elif hora <= 14 and n1 == 909:
    print("CONTESTAR")
    
#Solamente se contesta entre 17 y 19hrs
#exeptuando numeros que terminan en 877

if hora >= 17 and hora <= 19 and n2 != 877:
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and n2 == 877:
    print("NO CONTESTAR")

#Despues de las 19hrs , no contestar

if hora > 19:
    print("NO CONTESTAR")

#y si es en un horario fuera del rango

if hora > 14 and hora < 17:
    print("NO CONTESTAR")
