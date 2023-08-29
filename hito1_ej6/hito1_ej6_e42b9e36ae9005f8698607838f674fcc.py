commandData = int(input(""))
TempD = int(input(""))
TempE = int(input(""))
TempA = [commandData, TempD, TempE]
TempB = sorted(TempA)
TempC = str(TempB[0])
i = len(TempA)
x = 1
while x < i:
  TempC += "," + str(TempB[x])
  x += 1
print(TempC)