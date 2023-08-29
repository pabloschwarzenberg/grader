#Aprobación de créditos
i = int(input())
a = int(input())
n = int(input())
a_b = int(input())
e = input()
v = input()
if (a_b>=10 and n>=2) or (e=="C" and n>3 and a>=1972 and a<=1962) or (i>2500000 and e=="S" and v=="U") or (i>3500000 and a>5) or (v=="R" and e=="C" and n<2):
 print("APROBADO")
else:
  print("RECHAZADO")