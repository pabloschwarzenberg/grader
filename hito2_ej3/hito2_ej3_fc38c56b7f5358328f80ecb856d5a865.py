str=input()
n=int(input())
for i in str:
    print(i[0:n])
    print(i[n:len(str)])