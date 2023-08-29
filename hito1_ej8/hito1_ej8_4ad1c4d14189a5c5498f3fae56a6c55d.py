#Descomponer un número
print('** DESCOMPONER UN NÚMERO **')

n = int(input())
n_s = str(n)

lista_n = [] 
if len(n_s) > 4:
    False

else:
    p = 0
    while p < len(n_s):
        lista_n.append(n_s[p])
        p = p+1

    if len(lista_n) == 4:
        print(lista_n[0]+'M +'+' '+lista_n[1]+'C +'+' '+lista_n[2]+'D +'+' '+lista_n[3]+'U ')
    elif len(lista_n) == 3:
        print(lista_n[0]+'C +'+' '+lista_n[1]+'D +'+' '+lista_n[2]+'U ')
    elif len(lista_n) == 2:
        print(lista_n[0]+'D +'+' '+lista_n[1]+'U ')
    elif len(lista_n) == 1:
        print(lista_n[0]+'U ')