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
                print(vertex, current, height)
                if height_arr[current]:
                    height_arr[vertex] = height_arr[current] + height
                    print(height_arr)
                    break
        return max(height_arr)

    def fill_depth(self, parent, i, depth):
        if depth[i] != 0:
            return
        if parent[i] == -1:
            depth[i] = 1
            return

        if depth[parent[i]] == 0:
            self.fill_depth(parent, parent[i], depth)

        depth[i] = depth[parent[i]] + 1
        return

    def find_depth(self):
        depth = [0] * self.n
        for i in range(self.n):
            self.fill_depth(self.parent, i, depth)
        print(depth)

        return max(depth)

    def height(self):
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
    print(tree.height())

threading.Thread(target=main).start()
