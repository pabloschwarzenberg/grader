solucion = []
def backtracking(n, string = ""):
    global solucion
    global soluciones
    if len(string) == n:
        print(solucion[-1])
    else:
        for i in range(2):
            string += str(i)
            solucion.append(string)
            backtracking(n,string)
            solucion.pop(-1)
            string = string[0:-1]

n=int(input())
backtracking(n)