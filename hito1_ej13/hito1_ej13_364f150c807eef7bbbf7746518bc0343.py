#Factores Primos
a = int(input("numero: "))
lp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 ,97]
count = 0
while a != 1:
    xp = a % lp[count]
    if xp == 0:
        a = a/lp[count]
        print(lp[count])
    else:
        count = count + 1
