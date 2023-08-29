#Ordenar tres números

def bubble(arr):
    n = len(arr)
    for i in range(n):
            for j in range(0, n - i -1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

n1 = int(input('Digite el primer numero: '))
n2 = int(input('Digite el segundo numero: '))
n3 = int(input('Digite el tercer numero: '))

list = [n1, n2, n3]

list = bubble(list)

print('\n', list)