#Contestador de celular
cellphone_number = int(input("ingrese su numero telefonico del cual esta llamando: ")[0:8])
call_time = int(input("ingrese la hora en que llama y separe la hora por un punto: ")[0:4])
if (call_time >= 0) and (call_time <= 7):
    print ("contestar la llamada, puede ser una emergencia")
elif (call_time <= 2):
    print ("Contestar")
elif (call_time >= 17) and (call_time <= 19):
    print ("¡No contestar! Excepto si el numero comienza con 877")
elif (call_time >= 7) and (call_time < 14.00):
    print ("¡No contestar! Excepto si el numero comienza con 909")
elif (call_time > 19.00):
    print ("¡No Contestar!")
else:
    print ("Contestar la llamada de :" + str(call_time))