import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    arr = list(map(int, sys.stdin.readline().strip().split()))
    arr.sort()

    ans = -1
    for i in range(n):
        menores = i
        mayores = n - i - 1
        if menores == mayores:
            ans = arr[i]
            break

    print(ans)
