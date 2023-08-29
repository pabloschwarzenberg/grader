# por favor escribe aquí tu función
def es_primo(numero):
n=int(input())

d=2
primo=True
while d<n:
    if n%d==0:
        primo=False
        break
    d=d+1
if primo and n>1:
    print("True")
else:
    print("False")


