#Descomponer un número
a=int(input())
if 1000<=a<=9999:
  b=str(a)
  print(b[0]+"M","+",b[1]+"C","+",b[2]+"D","+",b[3]+"U")
elif 100<=a<=999:
  b=str(a)
  print(b[0]+"C","+",b[1]+"D","+",b[2]+"U")
elif 10<=a<=99:
  b=str(a)
  print(b[0]+"D","+",b[1]+"U")
elif 0<=a<=9:
  b=str(a)
  print(b[0]+"U")