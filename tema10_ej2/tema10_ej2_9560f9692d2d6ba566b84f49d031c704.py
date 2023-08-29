def levenshtein(palabra1, palabra2):
    n = len(palabra1) + 1
    m = len(palabra2) + 1
    distancia = [[0 for j in range(m)] for i in range(n)]
    for k in range(n):        
        distancia[k][0] = k
    for k in range(m):
        distancia[0][k] = k
    for i in range(1, n):
        for j in range(1, m):
            distancia[i][j] = min(distancia[i][j-1] + 1, distancia[i-1][j]+1, distancia[i-1][j-1] + (not palabra1[i-1] == palabra2[j-1]))
    d = distancia[n-1][m-1]
    if d > 1:
        return '+1'
    elif d == 0:
        return '0D'
    elif n != m:
        return 'IB'
    else:
        return '1S'

if __name__ == '__main__':
    tests = [['libro', 'libra'], ['libro', 'libros'], ['libro', 'espalda'], ['hola', 'hola']]
    for test in tests:
        print(levenshtein(*test))