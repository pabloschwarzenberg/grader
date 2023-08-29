#Ordenar tres números
N1=int(input("Ingrese el primer valor:"))
N2=int(input("Ingrese el segundo valor:"))
N3=int(input("Ingrese el tercer valor:"))
if N1<= N2<=N3:
  print(N1, "," ,N2,"," ,N3)
elif N1<= N3<=N2:
  print(N1, "," ,N3, "," ,N2)
elif N2<= N1 <=N3:
  print(N2, "," ,N1, "," ,N3)
elif N2<=N3<=N1:
  print(N2, "," ,N3, "," ,N1)
elif N3<=N1<=N2:
  print(N3, "," ,N1, "," ,N2)
elif N3<= N2<= N1:
  print(N3, "," ,N2, "," ,N1)