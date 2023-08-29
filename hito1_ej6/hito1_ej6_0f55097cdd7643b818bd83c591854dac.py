Val_A = int(input("Ingrese Primer Valor : "))
Val_B = int(input("Ingrese Segundo Valor : "))
Val_C = int(input("Ingress Tercer Valor : "))

# Rescata Valor Minimo
Val_Min = min(Val_A, Val_B, Val_C)

# Rescata Valor Maximo
Val_Mayor = max(Val_A, Val_B, Val_C)

# Rescata Valor Intermedio
Val_Inter = (Val_A + Val_B + Val_C) - Val_Mayor - Val_Min

print("Los Numeros ordenados son  : ", format(Val_Min) + ",", format(Val_Inter) + ",", format(Val_Mayor))