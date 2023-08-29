#Ordenar tres números
Val_1 = int(input("Ingrese Primer Valor : "))
Val_2 = int(input("Ingrese Segundo Valor : "))
Val_3 = int(input("Ingrese Tercer Valor : "))



#Rescata Valor Minimo
Val_Min = min(Val_1,Val_2,Val_3)



#Rescata Valor Maximo
Val_Max = max(Val_1,Val_2,Val_3)



#Rescata Valor Intermedio
Val_Inter = (Val_1 + Val_2 + Val_3)-Val_Max-Val_Min



print("Los Numeros ordenados son : ", format(Val_Min)+ ",", format(Val_Inter)+",", format(Val_Max))      