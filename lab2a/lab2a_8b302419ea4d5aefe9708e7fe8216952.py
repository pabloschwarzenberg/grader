#múltiplos
N_i = int(input("Ingrese número inicial:"))           
N_f = int(input("Ingrese número final:"))

for variable in range(N_i, N_f + 1):
    if variable%2 == 0 and variable%7 == 0:
        print(variable)    