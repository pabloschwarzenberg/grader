def buscarTodas(a,b):
    q=[]
    for x in range(len(a)):
        if a[x]==b:
            q.append(str(x))
    return " ".join(q)

if __name__ == "__main__":
    pass