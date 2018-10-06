S = list(input())
last = len(S)
chiwawa = []
for c in range(0,last):
    if 'c' in S[c]:
        for w1 in range(c+1, last):
            if 'w' in S[w1]:
                for w2 in range(w1+1, last):
                    if 'w' in S[w2]:
                        chiwawa.append(w2-c+1)
if chiwawa:
    print(min(chiwawa))
else:
    print(-1)
