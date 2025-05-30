n = int(input())
arr = list(map(int, input().split()))

stack = []
max_area = 0

for i, height in enumerate(arr):
    start = i
    while stack and stack[-1][1] > height:
        index, h = stack.pop()
        area = h * (i - index)
        max_area = max(max_area, area)
        start = index  # update start to left boundary
    stack.append((start, height))


for i, h in stack:
    area = h * (n - i)
    max_area = max(max_area, area)

print(max_area)
