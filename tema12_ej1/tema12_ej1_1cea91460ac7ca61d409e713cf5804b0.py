n=int(input())

def bt(n,sol=[],combinaciones=[]):
    if len(sol)==n:
        combinaciones.append(sol.copy())
        return
    for i in ["0","1"]:
        sol.append(i)
        bt(n,sol,combinaciones)
        sol.pop()
    return(combinaciones)

for bino in bt(n):
    print("".join(bino))


