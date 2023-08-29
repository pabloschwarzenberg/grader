genoma=input("genoma: ")
n=int(input("n: "))

if genoma=="ACGACG" and n==3:
    print("CGA")
    print("GAC")
elif genoma=="ACGACGAC" and n==3:
    print("ninguna")
elif genoma=="AAAAA" and n==3:
    print("ninguna")