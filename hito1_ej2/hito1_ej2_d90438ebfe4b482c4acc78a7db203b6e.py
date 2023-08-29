#Contestador de celular
Var_1 = str(input("ingrese su numero telefonico  ")) 
Var_2 = eval(input("ingrse la hora   "))
if  0 < Var_2 < 7:
  print("CONTESTAR")
elif Var_2 < 14:
  if "909" in Var_1:
    print("CONTESTAR")
  else:
    print("NO contestar")
elif 17 < Var_2 < 19 :
   if "877" in Var_1:
    print("NO CONTESTAR")
   else:
    print("contestar")
elif Var_2 > 19:
  print("NO CONTESTAR")
