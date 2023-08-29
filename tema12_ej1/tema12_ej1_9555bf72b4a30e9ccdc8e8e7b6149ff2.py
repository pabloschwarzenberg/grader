def backtrack(num,n):
    if len(num)==n:
        print(num)
        return
    num=siguiente(num,n)
    if num!=None:
        backtrack(num,n)
        num=alterno(num)
        backtrack(num,n)
        
def siguiente(num,n):
    if len(num)<n:
        return num+"0"
        
def alterno(n):
    return n[:-1]+"1"

n=int(input())
num=""
backtrack(num,n)
           