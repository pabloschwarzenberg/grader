##9.-numeros amigos
def divisores(num):
    vec=[]
    for i in range(1,num):
        if num % i==0:
            vec.append(i)
    return vec

def sumatoria(vec):
    sumatoria =0
    for k in vec:
        sumatoria=sumatoria + k
    return sumatoria

ingreso_a=""
ingreso_b=""
num_a=0
num_b=0
vec_a=[]
vec_b=[]
sum_a=0
sum_b=0

num_a=("ingrese un numero")
num_b=input("ingrese otro numero")

num_a=(ingreso_a)
num_b=(ingreso_b)

vec_a=divisores(num_a)
vec_b=divisores(num_b)

sum_a=sumatoria(vec_a)
sum_b=sumatoria(vec_b)


if sum_a==num_b and sum_b==num_a:
    print("son amigos")
else:
    print("no son amigos")
           