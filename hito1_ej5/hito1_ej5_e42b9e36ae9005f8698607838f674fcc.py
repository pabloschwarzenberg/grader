#Cálculo del dígito verificador de un rut
TempA = input("")
x = len(TempA)
TempF = "234567234567234567"[:x]
i = 0
TempB = 0
while i < x:
    TempB += int(TempA[i]) * int(TempF[x - i - 1])
    i += 1
TempC = TempB % 11
TempD = (11 - TempC) % 11
if (TempD == 10):
    TempE = "k"
else:
    TempE = str(TempD)
print("dv=" + TempE)