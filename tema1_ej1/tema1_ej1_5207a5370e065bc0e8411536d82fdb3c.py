#Suma de los N primeros números
print("Hola ingresa un numero para saber cual es la sunma de los N primeros numeros")
num=int(input())
num_sumado_por_sus_antecesores=num*(num+1)/2
print("La suma de los antecesores de ", num, "son",num_sumado_por_sus_antecesores)