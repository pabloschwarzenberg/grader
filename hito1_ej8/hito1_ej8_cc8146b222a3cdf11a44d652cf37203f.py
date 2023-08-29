valor = list(input("Ingresa un valor: "))

if len(valor) == 1:
    
    print(valor[0] + "U")

elif len(valor) == 2:  # ["1", "2"]
    print(valor[0] + "D +", valor[1] + "U")

elif len(valor) == 3:  # ["1", "2", "3"]
    print(valor[0] + "C +", valor[1] + "D +", valor[2] + "U")

elif len(valor) == 4:  # ["1", "2", "3", "4"]
    print(valor[0] + "M +", valor[1] + "C +", valor[2] + "D +", valor[3] + "U")