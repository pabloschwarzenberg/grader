#inp = str(input())
var = [0,0]
var[0] = int(input())
var[1] = int(input())
signos = ["aries", "tauro", "geminis", "cancer", "leo", "virgo","libra", "escorpion", "sagitario", "capricornio", "acuario", "piscis"]

dias = [21,20,21,21,22,21,22,22,23,22,23,23,24,23,24,22,23,21,22,20,21,19,20,20]
meses = []

inicial = 3
ind = 0
for x in range (len(dias)):
  meses.append(inicial)
  if ind % 2 == 0:
    inicial += 1
  ind += 1

nro = 0
for x in meses:
  if int(var[1]) == x:
    if int(var[0]) < dias[nro]:
      in_signo = nro - 1
    else:
      in_signo = nro
  nro += 1

in_signo = in_signo // 2
print(signos[in_signo])