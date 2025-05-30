n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):

        x1 = arr[i][j] > arr[i][j - 1] and arr[i][j] > arr[i][j + 1]
        x2 = arr[i][j] < arr[i - 1][j] and arr[i][j] < arr[i + 1][j]
        y1 = arr[i][j] < arr[i][j - 1] and arr[i][j] < arr[i][j + 1]
        y2 = arr[i][j] > arr[i - 1][j] and arr[i][j] > arr[i + 1][j]
        if (x1 and x2) or (y1 and y2):
            print(arr[i][j], end=" ")
            cnt += 1
    print()
print(cnt)
