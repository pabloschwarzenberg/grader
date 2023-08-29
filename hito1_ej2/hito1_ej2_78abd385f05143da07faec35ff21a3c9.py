#Contestador de celular
Numero_telefono=int(input("Ingresar un número de telefono que tenga 8 dígitos: "))
Hora_Dllamada=int(input("ingresar la hora de la llamada: "))

def contestar_llamadas(Numero_telefono, Hora_Dllamada):
   if Hora_Dllamada >=0 and Hora_Dllamada <= 7:
     return "Responder inmediatamente, emergencia"
   if Hora_Dllamada <= 14 and Numero_telefono % 100 == 909:
     return "Contestar si termina en 909"
   if Hora_Dllamada >= 17 and Hora_Dllamada <= 19 and Numero_telefono // 10000000 !=877:
     return "No responder las llamadas"
   else:
     print("no contestar")