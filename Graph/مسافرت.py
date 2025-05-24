# import sys
#
# sys.setrecursionlimit(10 ** 5 + 100)
#
# n = int(input())
#
# edges = [[] for _ in range(n)]
# mark = [False] * n
#
# arr = []
#
# for i in range(n):
#     arr.append(tuple(map(int, input().split())))
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if i == j:
#             continue
#         x1, y1 = arr[i]
#         x2, y2 = arr[j]
#         if x1 == x2 or y1 == y2:
#             edges[i].append(j)
#             edges[j].append(i)
#
# count = 0
# def DFS(n):
#     mark[n] = True
#     for i in edges[n]:
#         if not mark[i]:
#             DFS(i)
#
#
# for i in range(n):
#     if not mark[i]:
#         DFS(i)
#         count += 1
#
#
# print(count - 1)
#
#
#
#

n = int(input())
cordinates = []

for i in range(n):
    x, y = map(int, input().split())

    cordinates.append((x,y))

print(cordinates)

for i in range(len(cordinates)):
    print(cordinates[i])