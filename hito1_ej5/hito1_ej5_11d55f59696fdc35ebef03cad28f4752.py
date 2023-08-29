contador = 0
x = eval(input())
x = str(x)
x = list(x)
cont = 1
auxlst = []
for n in x:
    auxlst.append(x[len(x)-cont])
    cont += 1
x = auxlst
total = 0
for z in x:
    y = (contador%6)+2
    c = int(z)*y
    total += c
    contador += 1
aux = total//11
aux = total - (11*aux)
digito = 11 - aux
if digito == 11:
    digito = 0
elif digito == 10:
    digito = "k"
print("dv="+ str(digito))