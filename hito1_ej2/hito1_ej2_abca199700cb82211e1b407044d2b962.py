num = str(input("Ingrese el número telefonico: "))
hora = int(input("Ingrese la hora que se realizó la llamada: "))
if hora > 0 and hora < 7:
 print("SÍ CONTESTAR")
if hora > 19 and hora <= 23:
 print("NO CONTESTAR")
else:
 if hora > 7 and hora < 14 and str(num[-3]) == "9" and str(num[-2]) == "0" and str(num[-1]) == "9":
  print("sí contestar")
 if hora > 7 and hora < 14 and str(num[-3]) != "9" and str(num[-2]) != "0" and str(num[-1]) != "9":
  print("no contestar")
 if hora < 19 and str(num[0:1]) == "8" and str(num[1:2]) == "7" and str(num[2:3]) == "7":
  print("no contestar")
 if hora > 17 and hora < 19 and str(num[0:1]) != "8" and str(num[1:2]) != "7" and str(num[2:3]) != "7":
  print("sí contestar")