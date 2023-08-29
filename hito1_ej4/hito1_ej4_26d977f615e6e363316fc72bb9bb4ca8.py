numero=int(input())
def dectobin(numero):
  binnum=0
  power=0
  while numero>0:
    binnum += 10**power * (numero%2)
    numero //=2
    power +=1
    return binnum
    print(binnum)