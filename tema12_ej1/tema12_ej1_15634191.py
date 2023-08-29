n=int(input())
def binario(num):
    global n
    if len(num)<n:
        binario(num+"1")
        binario(num+"0")
    else:
        print(num)
binario("")


