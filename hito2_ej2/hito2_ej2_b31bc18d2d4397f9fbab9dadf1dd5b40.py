genoma = input("")
genoma = genoma.upper()
words_allowed = ["A", "C", "T", "G"]
count = 0
is_genoma = True
for i in genoma:
    for j in words_allowed:
        if i == j:
            count += 1
    if count > 0:
        count = 0
    else:
        is_genoma = False
        break
if is_genoma:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")