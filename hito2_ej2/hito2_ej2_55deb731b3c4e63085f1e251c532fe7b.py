g = input("Ingresa los genomas")
count = 0
for i in g:
    if i == 'A':
        count += 1
    elif i == 'C':
        count += 1
    elif i == 'T':
        count += 1
    elif i == 'G':
        count += 1
    else:
        print("secuencia incorrecta")
if count == 4:
    print('secuencia correcta')