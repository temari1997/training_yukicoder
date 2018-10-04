a = list(input())
print(a)
b,c = map(int, input().split())
a[b], a[c] = a[c], a[b]
print("".join(a))
