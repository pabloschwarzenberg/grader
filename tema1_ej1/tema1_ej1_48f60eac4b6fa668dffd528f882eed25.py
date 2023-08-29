#Suma de los N primeros números
variableN = -1
outcome = 0

while (variableN < 0):
    variableN = int(input(" ingrese un  numero natural: "))

outcome = variableN*(variableN + 1)/2
print(outcome)