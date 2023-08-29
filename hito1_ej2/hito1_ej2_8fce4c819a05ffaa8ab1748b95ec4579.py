#Contestador de celular
nt=int(input())
hr=int(input())
lista=[int(x) for x in str(nt)]
if (hr>=0 and hr<=7):
  print("CONTESTAR")
elif hr<=14 and lista[5]!=9 and lista[6]!=0 and lista[7]!=9:
  print("NO CONTESTAR")
elif hr<=14 and lista[5]==9 and lista[6]==0 and lista[7]==9:
  print("CONTESTAR")
elif hr>=17 and hr<=19 and lista[0]!=8 and lista[1]!=7 and lista[2]!=7:
  print("CONTESTAR")
elif hr>=17 and hr<=19 and lista[0]==8 and lista[1]==7 and lista[2]==7:
  print("NO CONTESTAR")
elif hr>19:
  print("NO CONTESTAR")


