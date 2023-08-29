import random
def binario(largo):
    a = ['0','1']
    if largo == 1:
        return random.choice(a)
    else:
        return random.choice(a) + binario(largo-1)

n = int(input('largo'))
lb = []
while len(lb) < 2**n:
    bin = binario(n)
    if bin not in lb:
        lb.append(bin)

for i in lb:
    print(i)