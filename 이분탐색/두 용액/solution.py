N = int(input())

liquids = list(map(int, input().split()))
liquids = sorted(liquids)

left = 0
right = N - 1

answer = float("inf")
final = []

while left < right:
    total = liquids[left] + liquids[right]

    if abs(total) < answer:
        answer = abs(total)
        final = [liquids[left], liquids[right]]

    if total < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])