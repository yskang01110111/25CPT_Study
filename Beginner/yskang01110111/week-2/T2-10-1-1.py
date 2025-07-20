n = int(input())
blocks = [
    int(input())
    for _ in range(n)
]

sum_of_blocks = sum(blocks)

avg = sum_of_blocks // n
ans = 0
for block_num in blocks:
    if block_num > avg:
        ans += block_num - avg

print(ans)
