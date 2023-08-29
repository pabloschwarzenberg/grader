def backtracking(n,resultado):
    if len(resultado) == n:
        print(resultado)
        return
    if len(resultado) > n:
        return
    else:
      backtracking(n,resultado + "1")
      backtracking(n,resultado + "0")
      return resultado
        
n = int(input())
print(backtracking(n,""))