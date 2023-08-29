#Aprobación de créditos
ingreso = int(input())
an = int(input())
nh = int(input())
apb = int(input())
ec = input()
lda = input()
if apb > 10 and nh >= 2:
  print("APROBADO")
elif ec.lower() == "c" and nh > 3 and 45 <= an <= 55:
  print("APROBADO")
elif ingreso > 2500000 and ec.lower() == "s" and lda.lower() == "u":
  print("APROBADO")
elif ingreso > 3500000 and apb > 5:
  print("APROBADO")
elif lda.lower() == "r" and ec.lower() == "c" and nh < 2:
  print("APROBADO")
else:
  print("RECHAZADO")