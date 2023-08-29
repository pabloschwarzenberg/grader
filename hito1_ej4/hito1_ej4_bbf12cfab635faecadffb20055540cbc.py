import math
b = int(input("Ponga le número: "))
bin=""
while (b>0):
    if (b % 2) == 0:
        bin = "0" + bin
    else:
        bin = "1" + bin
    b = int(math.floor(b / 2))
print("Resultado="+bin)