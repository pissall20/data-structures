# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    queue = deque()
    maximums = []
    length = len(sequence)

    for i in range(length):
        while queue and sequence[i] >= sequence[queue[-1]]:
            queue.pop()
        queue.append(i)
        if queue and i >= m and queue[0] == i - m:
            queue.popleft()
        if i >= m - 1:
            maximums.append(sequence[queue[0]])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

