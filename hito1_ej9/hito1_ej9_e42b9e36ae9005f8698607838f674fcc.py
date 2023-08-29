#Sistema de Ecuaciones
TempG = float(input(""))
TempI = float(input(""))
TempK = float(input(""))
TempH = float(input(""))
TempJ = float(input(""))
TempL = float(input(""))
if TempJ * TempG != TempI * TempH:
    x = (TempI * TempL - TempJ * TempK) / (TempI * TempH - TempJ * TempG)
else:
    x = "Indeterminado / indefinido"
if TempJ * TempG != TempI * TempH:
    i = (TempL * TempG - TempH * TempK) / (TempJ * TempG - TempI * TempH)
else:
    i = "Indeterminado / indefinido"
command = ["x=" + str(round(x, 1)), "y=" + str(round(i, 1))]
print(list(command))
