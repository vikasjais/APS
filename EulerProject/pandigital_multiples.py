eights = [i for i in range(1,9)]
nines = [i for i in range(1,10)]

e = []
ni = []

for i in range(9,10**5):
    aux = ""
    for j in eights:
        if len(aux) > 7:
            break
        aux += str(i * j)
    aux = list(map(int,aux))
    aux.sort()
    if aux == nines:
        ni.append(i)
    elif aux == eights:
        e.append(i)
        
n,w = map(int,input().strip().split(' '))
if w == 8:
    print('\n'.join(list(map(str,filter(lambda x: x <= n,e)))))
else:
    print('\n'.join(list(map(str,filter(lambda x: x <= n,ni)))))