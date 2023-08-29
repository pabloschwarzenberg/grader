numer=input("Ingrese un número")
if int(numer)>=1000:
  print(numer[-4]+"M" +" + "+numer[-3]+"C" +" + "+numer[-2]+"D" +" + "+ numer[-1]+"U")
if int(numer)>=100 and int(numer)<1000:
  print(numer[-3]+"C" +" + "+numer[-2]+"D" +" + "+ numer[-1]+"U")
if int(numer)>=10 and int(numer)<100:
  print(numer[-2]+"D" +" + "+ numer[-1]+"U")
if int(numer)>=1 and int(numer)<10:
  print(numer[-1]+"U")