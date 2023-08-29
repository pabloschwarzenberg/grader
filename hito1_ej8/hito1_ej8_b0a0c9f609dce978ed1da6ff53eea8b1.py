#Descomponer un número
numero = input()
rev_numero = numero[::-1]
lista = ['U','D', 'C', 'M']
res = ''
for num in range(0, len(rev_numero)):
    if(num == 0):
        res = rev_numero[num] + lista[num] + res
    else:
        res = rev_numero[num] + lista[num] + " + "+ res
print(res)