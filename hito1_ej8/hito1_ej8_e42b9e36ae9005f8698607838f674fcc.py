#Descomponer un número
TempA = input("")
TempB = TempA[-1::1] + "U"
TempC = len(TempA)
if TempC > 1 and TempA[-2::2] != "0":
  TempB = TempA[-2::2] + "D + " + TempB
if TempC > 2 and TempA[-3::3] != "0":
  TempB = TempA[-3::3] + "C + " + TempB
if TempC > 3 and TempA[-4::4] != "0":
  TempB = TempA[-4::4] + "M + " + TempB
print(TempB)