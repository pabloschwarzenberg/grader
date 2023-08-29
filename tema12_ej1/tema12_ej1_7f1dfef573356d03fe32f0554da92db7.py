import random
class bina:
    def __init__(self):
        self.combinaciones = []
        self.candidatos = []
    def soluciones(self,n):
        soluciones = self.combinaciones
        i = 0
        j = n
        while i <= n and j >= 0:
            a = j * "0"
            b = i * "1"
            soluciones.append(a+b)
            self.activar_backtracking(a+b,n)
            i+=1
            j-=1
        self.combinaciones = soluciones
        self.imprimir()
    def agregar_combinaciones(self):
        c = self.combinaciones
        c.append(self.candidatos)
        self.combinaciones = c
        self.candidatos = []
    def agregar_candidato(self,candidato):
        c = self.candidatos
        c.append(candidato)
        self.candidatos = c
    def imprimir(self):
        for l in self.combinaciones:
            print(l) #se imprime (n+1)num_permutaciones
    def num_permutaciones(self,sol):
        n = len(sol)
        c = 0
        u = 0
        for i in list(sol):
            if i == "0":
                c+=1
            else:
                u+=1
        num_permutaciones = factorial(n)/(factorial(u) * factorial(c))
        return num_permutaciones
    def generar_candidato(self,sol):
        l = list(sol)
        random.shuffle(l)
        return ''.join(l)
    def backtracking(self,sol,n_p,candidato=""):
        candidato = self.generar_candidato(sol)
        for l in self.candidatos:
            if candidato == l:
                break
            else:
                self.agregar_candidato(candidato)
                break
        if len(self.candidatos) == n_p:
            self.agregar_combinaciones()
            return
        else:
            self.backtracking(sol,n_p)
    def factorial(x):
        if x == 1:
            return 1
        else:
            return x * self.factorial(x-1)
    def activar_backtracking(self,sol,n):
        self.backtracking(sol,self.num_permutaciones(sol))
def factorial(x) :
    j = 1
    for i in range (1,x+1) :
        j *= i
    return j
    
BB = bina()
BB.soluciones(int(input()))