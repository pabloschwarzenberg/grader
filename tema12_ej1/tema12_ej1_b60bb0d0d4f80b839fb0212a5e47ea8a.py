n=int(input())
def bina(n):
    if n==1:
        return ([i for i in ["0","1"]])
    else:
        return [i+r for i in ["0","1"] for r in bina(n-1)]
for com in bina(n):
  print(com)

           