#Contestador de celular
telnum = int(input())
hr = int(input())
if 9999999 < telnum <= 99999999:
  num = telnum % 1000
  if 0 < hr < 24:
    if 0 < hr <= 7:
      print("CONTESTAR")
    elif 17 <= hr <= 19 and num == 877:
      print("CONTESTAR")
    elif hr >= 19:
      print("NO CONTESTAR")
    elif 7 < hr < 14 and num == 909:
      print("CONTESTAR")
    else:
      print("NO CONTESTAR")