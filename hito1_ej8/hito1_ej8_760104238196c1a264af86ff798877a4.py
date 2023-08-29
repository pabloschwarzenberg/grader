#Descomponer un número
x = input()
lsta = ['U', 'D', 'C', 'M']
resp = []
res2 = []
sol = ''
for i in x:
    resp.insert(0, i)
for i in range(len(resp)):
    resp[i] += lsta[i]
for i in resp:
    res2.insert(0,i)
for i in res2:
    sol += i + ' + '
print(sol[:-3])