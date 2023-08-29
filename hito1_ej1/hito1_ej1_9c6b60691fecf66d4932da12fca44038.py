#Nota final

PT = eval(input("NOTA PT: "))
PI = eval(input("NOTA PI: "))
NE = eval(input("NOTA NE: "))
PP = eval(input("NOTA PP: "))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

round(NF,1)

print("Nota Final:",NF)     