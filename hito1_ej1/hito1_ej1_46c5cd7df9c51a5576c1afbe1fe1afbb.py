#Nota final
PT = float(input("Ingrese su primera nota: "))
PI = float(input("Ingrese su segunda nota: "))
NE = float(input("Ingrese su tercera nota: "))
PP = float(input("Ingrese su cuarta nota: "))

promedio = (0.3*PT) + (0.3*PI)+(0.3*NE)+(0.1*PP)
promedio_redondeado = round(promedio,1)
print(promedio_redondeado)  