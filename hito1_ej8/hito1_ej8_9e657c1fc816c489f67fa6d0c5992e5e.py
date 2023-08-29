#Descomponer un número
num = int(input("Numero: "))
snum = str(num)
lsnum = len(str(num))

if lsnum == 1:
  print(snum+"U")

elif lsnum == 2:
  print(snum[0]+"D + "+snum[1]+"U")

elif lsnum == 3:
  print(snum[0]+"C + "+snum[1]+"D + "+snum[2]+"U")

elif lsnum == 4:
  print(snum[0]+"M + "+snum[1]+"C + "+snum[2]+"D + "+snum[3]+"U")