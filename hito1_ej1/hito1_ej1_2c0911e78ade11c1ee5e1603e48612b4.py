#Nota final
PT = float(input(range(1,8)))
PI = float(input(range(1,8)))
NE = float(input(range(1,8)))
PP = float(input(range(1,8)))
round(PT,1)
round(PI,1)
round(NE,1)
round(PP,1)
F = 0.3*(PT + PI + NE) + 0.1*PP
print(round(F, 1))
