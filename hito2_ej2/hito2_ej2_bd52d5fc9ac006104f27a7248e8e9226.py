genoma = input()
genoma=genoma.upper()
adn = ("ACTG")
count = 0
for i in genoma:
    if i in adn:
        count += 1
if count == len(genoma):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")

