def alinear(x,y):
    x = x.upper()
    y = y.upper()
    sec_alineada = []
    i = 0
    j = 0
    while j<len(y):
        while i<len(x):
            if x[i]==y[j]:
                sec_alineada.append(y[j])
                i =i+1
                break
            else:
                sec_alineada.append('_')
                i = i+1
        if i==len(x):
            j = j+1
            i = i+1
        if i>len(x):
            sec_alineada.append(y[j])
        j = j+1
    string_sa = ''.join(sec_alineada)
    return string_sa

secc1 = input('Ingrese la primera secuencia de ADN: ')
secc2 = input('Ingrese la segunda secuencia de ADN: ')
print(alinear(secc1,secc2))