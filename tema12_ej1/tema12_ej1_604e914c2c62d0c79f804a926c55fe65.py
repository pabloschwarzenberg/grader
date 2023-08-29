def binario(n):
    if n==1:
        return([i for i in["0","1"]])
    else:
        return([i+j for i in ["0","1"] for j in binario(n-1)])



n=int(input(":"))
print("""
""".join(binario(n)))        