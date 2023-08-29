#Ordenar tres números
num_1 = int(input("Ingrese el primer número:"))
num_2 = int(input("Ingrese el segundo número:"))
num_3 = int(input("INgrese el tercer número:"))

if num_1 > num_2:
    v_aux = num_1
    num_1 = num_2
    num_2 = v_aux

if num_2 > num_3:
    v_aux = num_2
    num_2 = num_3
    num_3 = v_aux

if num_3 > num_1:
    v_aux = num_3
    num_3 = num_1
    num_1 = v_aux

if num_1 > num_2:
    v_aux = num_1
    num_1 = num_2
    num_2 = v_aux

if num_2 > num_3:
    v_aux = num_2
    num_2 = num_3
    num_3 = v_aux

if num_1 > num_2:
    v_aux = num_1
    num_1 = num_2
    num_2 = v_aux

print(num_1, end=",")
print(num_2, end=",")
print(num_3)