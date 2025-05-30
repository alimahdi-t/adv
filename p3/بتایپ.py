s = input()
stack = []
for i in s:
    if i == "=":
        if stack:
            stack.pop()
    else:
        stack.append(i)

print("".join(stack))
