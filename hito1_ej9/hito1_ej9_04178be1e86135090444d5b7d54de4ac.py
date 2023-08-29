#Sistema de Ecuaciones
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

sx1 = x1 * x2
sx2 = x2 * -x1

sy1 = y1 * x2
sy2 = y2 * -x1

sr1 = r1 * x2
sr2 = r2 * -x1

y = sy1 + sy2
r = sr1 + sr2
y = float(y * r)
x = float((sr1 - y1 * y)/sx1)
print("['x=" + str(x) + "', 'y="+str(y)+"']")