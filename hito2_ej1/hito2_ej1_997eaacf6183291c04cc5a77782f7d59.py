sec1 = list(input("Ingresa una secuencia: ").strip())
sec2 = list(input("Ingresa una secuencia: ").strip())
i=0
for letra in sec1:
    if letra != sec2[i]:
        sec2.insert(i,'_')
    i += 1
print("".join(sec1))
print("".join(sec2))      