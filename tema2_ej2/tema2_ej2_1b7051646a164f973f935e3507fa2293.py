ingreso_a = ""
ingreso_b = ""
num_a = 0
num_b = 0
vec_a = []
vec_b = []
sum_a = 0
sum_b = 0

ingreso_a = int(input("Ingrese un numero"))
ingreso_b = int(input("Ingrese otro numero"))

#convertir de string a int
num_a = int(ingreso_a)
num_b = int(ingreso_b)

#Funcion Divisores
def divisores(num):
    vec = []
    for i in range(1, num):
        if num % i == 0:
            vec.append(i)
    return vec

vec_a = divisores(num_a)
vec_b = divisores(num_b)

#Funcion Sumatoria
def sumatoria(vec):
    sumatoria = 0
    for c in vec:
        sumatoria = sumatoria + c
    return sumatoria

sum_a = sumatoria(vec_a)
sum_b = sumatoria(vec_b)

if sum_b == num_a and sum_a == num_b:
    print(True)
else:
    print(False)