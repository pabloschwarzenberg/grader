seq = input("Secuencia: ")
largo = int(input("Largo: "))
ss = []

tmp = []
res = []

for i in range(len(seq) - largo + 1):
    tmp.append(seq[i:i+largo])


for s in tmp:
    cnt = tmp.count(s)
    if cnt == 1:
        res.append(s)




if len(res) == 0:
    print("ninguna")

for subseq in res:
    print(subseq)