#Nota final
PT = float(input())
PI = float(input())
NE = float(input())
PP = float(input())

PTF = 0.3 * PT
PIF = 0.3 * PI
NEF = 0.3 * NE
PPF = 0.1 * PP

PF = PTF + PIF + NEF + PPF
print(round(PF,1))