i = int(input())
suf = ["M", "C", "D", "U"]
num = [int(x) for x in str(i)]

lar = len(str(i))
str1 = ""
ind = 4-lar
for item in num:
    if ind != 4-lar:
        str1 += " + "
    str1 += str(item) + suf[ind]
    ind += 1

print(str1)
