a = input()
b = int(input())
c = "contestar"
d = "no contestar"
numero = []
ex1 = ["9", "0", "9"]
ex2 = ["8", "7", "7"]
for n in a:
    numero.append(n)

if 0 <= b <= 7:
    print(c)
elif b < 14 and numero[5] == ex1[0] and numero[6] == ex1[1] and numero[7] == ex1[2]:
    print(c)
elif b > 19 and numero[0] == ex2[0] and numero[1] == ex2[1] and numero[2] == ex2[2]:
    print(c)
elif b == 18:
    print(d)
else:
    print(d)