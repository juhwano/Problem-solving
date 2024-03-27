from collections import deque

test_cases = int(input())
for _ in range(test_cases):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    queue = deque([(i, idx) for idx, i in enumerate(queue)])
    count = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.rotate(-1)