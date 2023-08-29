rut = input("ingrese rut: ")
contador = 2
total = 0
dv = 0

rutInvertido = rut[::-1]

for i in range(0,len(rut)):
  
  total += contador*int((rutInvertido)[i])
  if(contador == 7):
    contador = 2
    continue
  contador += 1

dv = 11-(total-((total // 11)*11))

if(dv == 11):
  dv = 0

if(dv == 10):
  dv = "k"


print("dv=",dv)  