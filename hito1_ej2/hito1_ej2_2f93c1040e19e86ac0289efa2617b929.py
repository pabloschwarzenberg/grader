#Contestador de celular
Num = input(">>>ingrese numero telefonico: ")
Hora = int(input(">>>ingrese hora de la llamada: "))
if 0 <= Hora <= 7:
    print(">>>Resultado:CONTESTAR")
elif Num[5:8] == str(909):
    print(">>>Resultado:CONTESTAR")
elif Hora < 14:
    print(">>>Resultado:NO CONTESTAR")
elif Hora < 17: 
    print("Resultado:NO CONTESTAR")
elif Num[0:3] == str(877):
    print("Resultado:NO CONTESTAR")
elif 17 <= Hora <= 19:
    print("Resultado:CONTESTAR")
elif Hora > 19:
    print("Resultado:NO CONTESTAR")     
      