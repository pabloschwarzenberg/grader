#Factores Primos
asd = int(input())
for a in range(2, asd):
    while asd/a == asd//a:
        asd= asd/a
        print(a)
if asd == 2:
  print(2)