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
        depth = [1] * self.n
        for i, num in enumerate(self.parent):
            while num != -1:
                depth[i] += 1
                num = self.parent[num]
        return max(depth)


def main():
    tree = TreeHeight()
    tree.read()
    # print(tree.compute_height())
    print(tree.compute_height())

threading.Thread(target=main).start()
