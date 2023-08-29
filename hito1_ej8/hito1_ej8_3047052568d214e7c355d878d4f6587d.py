#Descomponer un número
print("ingrese un numero ")
a=str(input(": "))
b=[a]
if len(a)==4:
  for i in b:
    print ((i[0]+"M +"),(i[1]+"C +"),(i[2]+"D +"),(i[3]+"U"))
if len(a)==3:
  for i in b:
    print ((i[0]+"C +"),(i[1]+"D +"),(i[2]+"U"))
if len(a)==2:
  for i in b:
    print ((i[0]+"D +"),(i[1]+"U"))    
elif len(a)==1:
  for i in b:
    print(i[0]+"U")      