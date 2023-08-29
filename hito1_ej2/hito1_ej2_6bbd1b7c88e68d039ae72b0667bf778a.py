#Contestador de celular
number = str(input("Ingrese el contacto: "))
tim = int(input("A que hora crees que te llamará: "))
if tim > 0 and tim < 7:
  print("CONTESTAR")
if tim > 19 and tim <= 23:
  print("NO CONTESTAR")
else:
  if tim > 7 and tim < 14 and str(number[-3]) == "9" and str(number[-2]) == "0" and str(number[-1]) == "9":
    print("CONTESTAR")
  if tim > 7 and tim < 14 and str(number[-3]) != "9" and str(number[-2]) != "0" and str(number[-1]) != "9":
    print("NO CONTESTAR")
  if tim > 17 and tim < 19 and str(number[0:1]) == "8" and str(number[1:2]) == "7" and str(number[2:3]) == "7":
    print("NO CONTESTAR")
  if tim > 17 and tim < 19 and str(number[0:1]) != "8" and str(number[1:2]) != "7" and str(number[2:3]) != "7":

    print("CONTESTAR")      