"""
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
"""    
e = [18, 78, 1728, 1764, 1782, 1827, 2178, 2358, 2718, 2817, 3564, 3582, 4176, 4356]
ni = [9, 192, 219, 273, 327, 6729, 6792, 6927, 7269, 7293, 7329, 7692, 7923, 7932, 9267, 9273, 9327]

n,w = map(int,input().strip().split(' '))
if w == 8:
    print('\n'.join(list(map(str,filter(lambda x: x <= n,e)))))
else:
    print('\n'.join(list(map(str,filter(lambda x: x <= n,ni)))))
