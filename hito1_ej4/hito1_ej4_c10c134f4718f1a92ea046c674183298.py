x=float(input("ingrese un numero:"))
if x <= 0:
    print("En binario es:",int (x),"")
B=""
while x > 0 :
    R=int(x%2)
    x=int(x/2)
    B=str(R)+B
print ("resultado=",B,"")