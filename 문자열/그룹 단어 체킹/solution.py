word_list = []
num = int(input())

for _ in range(num):
    word_list.append(input())

for word in word_list:
    stack = []
    for c in word:
        if stack:
            if stack[-1] == c:
                continue
            else:
                if c in stack:
                    num -= 1
                    break
                else:
                    stack.append(c)
        else:
            stack.append(c)
    
print(num)