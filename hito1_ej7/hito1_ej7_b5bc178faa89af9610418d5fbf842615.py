signo= ["capricornio","acuario","picis","aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario"]
fecha=[20,19,21,20,21,21,23,23,23,23,22,22]
día=int(input("día de nacimiento:"))
mes=int(input("mes de nacimiento:"))


mes= mes-1
if día>fecha[mes]:
  mes = mes+1
if mes ==12:
    mes=0
print("su signo es", signo[mes])   