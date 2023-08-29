print("Ingrese a continuacion su número teléfonico y la hora de llamada")
n=int(input("Número teléfonico:>"))
print("La Hora se escribe en enteros entre 0 y 23")
h=int(input("Hora de llamada:>"))
j=n%1000
if(n<10000000)or(n>99999999):
  print("Tu número de teléfono es invalido, favor ingresar uno de 8 números")
elif(h>=0 and h<=7):
    print("CONTESTAR")
elif(h>19 and h<24):
  print("NO CONTESTAR") 
elif(h>23):
 print("ingrese una hora valida, entre el rango de 0 a 23 horas")
elif(h>=17 and h<=19)and(n>=87700000 and n<=87799999):
  print("NO CONTESTAR") 
elif(h>7 and h<14)and(j==909):
 print("CONTESTAR")
elif(h>7 and h<14):
  print("NO CONTESTAR")
else:
 print("CONTESTAR")
      