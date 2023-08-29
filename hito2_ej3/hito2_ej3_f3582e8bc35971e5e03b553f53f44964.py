sec=input()
n=int(input())
L=len(sec)
if L%n==0:
    cantidad=L//n
    sec1=sec[0:cantidad]
    print(sec)
else:
    print("ninguna")