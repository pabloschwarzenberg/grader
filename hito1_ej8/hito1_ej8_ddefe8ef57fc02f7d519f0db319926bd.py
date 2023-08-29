#Descomponer un número
n = ((input("ingrese un numero ")))
if ( int(n) >= 1000):
    print( n[-4] + "M +", n[-3] + "C +", n[-2] + "D +", n[-1] + "U" )
elif ( int(n) >= 100):
    print(n[-3] + "C +", n[-2] + "D +", n[-1] + "U" )
elif ( int(n) >= 10):
    print( n[-2] + "D +", n[-1] + "U" )
elif ( int(n) >= -1):
    print( n[-1] + "U" )

