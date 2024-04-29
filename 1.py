counter = 0
with open('9.txt', 'r') as f:
    f = [i[:-1].split('\t') for i in f.readlines()]
    for i in range(len(f)):
        for g in range(len(f[i])):
            f[i][g] = int(f[i][g])
    for i in range(len(f)):
        l = set(f[i])
        if len(l) == 4:
            sum1 = 0
            sum2 = 0
            for j in l:
                if f[i].count(j) == 2:
                    sum1 += j
                elif f[i].count(j) == 1:
                    sum2 += j
            if sum1 > sum2:
                counter += 1
    print(counter)

# a = [6, 2, 3, 2, 3, 4]
# l = set(a)
# sum1 = 0
# sum2 = 0
# for j in l:
#     if a.count(j) == 2:
#         sum1 += j
#     elif a.count(j) == 1:
#         sum2 += j
# print(sum1)
# print(sum2)