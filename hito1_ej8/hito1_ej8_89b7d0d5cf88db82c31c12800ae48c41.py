print("ingrese N°: ")
gato= 0

gato=str(input(": "))

b=[gato]

if len(gato)==4:
  for i in b:
    print ((i[0]+"M +"),(i[1]+"C +"),(i[2]+"D +"),(i[3]+"U"))
if len(gato)==3:
  for i in b:
    print ((i[0]+"C +"),(i[1]+"D +"),(i[2]+"U"))
if len(gato)==2:
  for i in b:
    print ((i[0]+"D +"),(i[1]+"U"))
elif len(gato)==1:
  for i in b:
    print(i[0]+"U")