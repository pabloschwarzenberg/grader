binario = []
def binarios(largo):
    global binario
    if largo==0:
        print(''.join(binario))
    else:
        for i in range(0,2):
            binario.append(str(i))
            binarios(largo-1)
            binario=binario[:-1]
largo=int(input())
binarios(largo)