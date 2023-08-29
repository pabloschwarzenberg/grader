from random import *
def subseq(adn,n):
    ind = n
    if(len(adn)%n==0):
        adn.lower()
        print("{}".format(adn[0:ind]))
        print("{}".format(adn[ind:]))
    else:
        print("ninguna")

adn = input("Ingrese su genoma: ")
n = int(input("Ingrese el numero: "))
subseq(adn,n)