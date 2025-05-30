n = int(input())
keys = list(map(int, input().split()))
states = list(map(int, input().split()))

result = []

for i in range(n):
    if states[i] == 1:
        result.append(keys[i])

for i in sorted(result):
    print(i, end=" ")
