x = str(input("Ingrese numero telefonico:"))

z = int(input("Ingrese hora de la llamada:"))

if z > 0 and z < 7:

  print("CONTESTAR")

if z > 19 and z <= 23:

  print("NO CONTESTAR")

else:

  if z > 7 and z < 14 and str(x[-3]) == "9" and str(x[-2]) == "0" and str(x[-1]) == "9":

    print("CONTESTAR")

  if z > 7 and z < 14 and str(x[-3]) != "9" and str(x[-2]) != "0" and str(x[-1]) != "9":

    print("NO CONTESTAR")

  if z > 17 and z < 19 and str(x[0:1]) == "8" and str(x[1:2]) == "7" and str(x[2:3]) == "7":

    print("NO CONTESTAR")

  if z > 17 and z < 19 and str(x[0:1]) != "8" and str(x[1:2]) != "7" and str(x[2:3]) != "7":

    print("CONTESTAR")


        

        
