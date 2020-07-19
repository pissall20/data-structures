# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        height_arr = [0] * self.n
        root = self.parent.index(-1)
        height_arr[root] = 1
        for vertex in range(self.n):
            height = 0
            current = vertex
            while current != -1:
                height += 1
                current = self.parent[current]
                if height_arr[current]:
                    height_arr[vertex] = height_arr[current] + height
                    break
        return max(height_arr)


def main():
    tree = TreeHeight()
    tree.read()
    # print(tree.compute_height())
    print(tree.compute_height())

threading.Thread(target=main).start()
