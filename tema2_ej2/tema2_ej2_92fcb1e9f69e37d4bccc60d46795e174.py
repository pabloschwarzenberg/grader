# completa el código de la función
numUno = 2
numDos = 3

def amigos(x,y):
    sumax = 0
    sumay = 0
    for i in range(1,x):
        if x % i == 0:
            sumax+=i
    for k in range(1,y):
        if y % k == 0:
            sumay+= k
    return sumax == y and sumay == x
if amigos(numUno, numDos):
    print ("¡Son amigos!")
else:
    print ("No son amigos")        