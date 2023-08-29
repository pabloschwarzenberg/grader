num=int(input("Ingrese numero de telefono:\n"))
hrs=int(input("Hora de llamada:\n"))

strnum=str(num)
len(strnum)
if len(strnum)==8:
  a=float(strnum[5])
  b=float(strnum[6])
  c=float(strnum[7])

#strhrs=str(hrs)
if len(strnum)>9:
  print("Numero mayor a 8 digitos no se lee")
elif hrs<=7 and hrs>=0:
  print("CONTESTAR")
elif hrs>7 and hrs<14 and a==9 and b==0 and c==9:
  print("CONTESTAR")

elif hrs>17 and hrs<19 and a==8 and b==7 and c==7:
  print("CONTESTAR")
elif hrs<19 and hrs>14 and not a==8 and b==7 and c==7:
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
