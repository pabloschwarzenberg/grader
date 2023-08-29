number = str(input("Holi ingresa un número telefónico de ocho dígitos: "))
Hour = int(input("Ingresa el registro de la hora en que ocurrió la llamada owo: "))
#Definir directrices
if(0 <= Hour <= 7):
  print("Contestar owo")
elif(14 <= Hour <= 16):
  print("No contestar uwun`t")
elif(8 <= Hour <= 14):
  if str(number[-3]) == "9" and str(number[-2]) == "0" and str(number[-1]) == "9":
    print("Contestar owo")
  else:
    print("No contestar uwun´t")
elif(17 <= Hour <= 19):
  if str(number[-3]) == "8" and str(number[-2]) == "7" and str(number[-1]) == "7":
    print("Contestar owo")
  else:
    print("No contestar uwun´t")
elif(20 <= Hour):
  print("No contestar uwun´t")
else:
  print("No contestar uwun´t")
print("Chaín bombin")