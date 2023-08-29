#Contestador de celular
TempA = input("")
TempB = int(input(""))
if 0 <= TempB % 24 <= 7:
  print("CONTESTAR")
elif TempB % 24 < 14:
  if TempA[-3:] == "909":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif 17 <= TempB % 24 <= 19:
  if TempA[:3] == "877":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif TempB % 24 > 19:
  print("NO CONTESTAR")