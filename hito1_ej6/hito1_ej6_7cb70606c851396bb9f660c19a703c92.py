#Ordenar tres números
print("ingresar el primer numero: ")
n1 = int(input())
print("ingresar el segundo numero: ")
n2 = int(input())
print("ingresar el tercero numero: ")
n3 = int(input())
if(n1<=n2 and n2<=n3):
  print("",n1," , ",n2," , ",n3)
elif(n2<=n1 and n1<=n3):
  print("",n2," , ",n1," , ",n3)
elif(n3<=n1 and n1<=n2):
  print("",n3," , ",n1," , ",n2)
elif(n3<=n2 and n2<=n1):
  print("",n3," , ",n2," , ",n1)
elif(n1<=n3 and n3<=n2):
  print("",n1," , ",n3," , ",n2)
elif(n2<=n3 and n3<=n1):
  print("",n2," , ",n3," , ",n1)      