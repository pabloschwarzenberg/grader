Val_A = int(input("Ingrese Primer Valor : "))
Val_B = int(input("Ingrese Segundo Valor : "))
Val_C = int(input("Ingrese Tercer Valor : "))

#Rescata Valor Minimo
Val_Minimo = min(Val_A,Val_B,Val_C)

#Rescata Valor Maximo
Val_Maximo = max(Val_A,Val_B,Val_C)

#Rescata Valor Intermedio
Val_Inter = (Val_A + Val_B + Val_C)-Val_Maximo-Val_Minimo

print("Los Numeros ordenados son : ", format(Val_Minimo)+ ",", format(Val_Inter)+",", format(Val_Maximo))
