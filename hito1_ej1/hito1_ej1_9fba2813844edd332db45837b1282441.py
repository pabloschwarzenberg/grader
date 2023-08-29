#Nota final
import math
PT = eval(input(""))
PI = eval(input(""))
NE = eval(input(""))
PP = eval(input(""))
promedioFinal =PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
promedioFinal = promedioFinal * 10
promedioFinal = math.ceil(promedioFinal)
promedioFinal = promedioFinal / 10
print(promedioFinal)