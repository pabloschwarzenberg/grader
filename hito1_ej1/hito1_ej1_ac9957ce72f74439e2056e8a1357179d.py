#Nota final
PT = eval(input("Input tasks points: "))
PI = eval(input("Interrogation points: "))
NE = eval(input("Test points: "))
PP = eval(input("Presentation points: "))
fAvg = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print("Your final grade is {}.".format(round(fAvg,1)))