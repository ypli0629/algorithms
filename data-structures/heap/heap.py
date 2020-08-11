"""
堆
"""


class Heap:
    def __init__(self):
        self._heap = [None]
        self._size = 0

    @property
    def heap(self):
        return self._heap

    @property
    def size(self):
        return self._size

    def insert(self, value):
        """
        插入元素
        :param value:
        """
        self._heap.append(value)
        self._size += 1

        self._shift_up(self._size)

    def shift(self):
        """
        移除堆顶
        """
        self._swap(1, self._size)
        node = self._heap.pop()
        self._size -= 1

        self._shift_down(1, self._size)
        return node

    def sort(self):
        """
        堆排序
        """
        i = self._size
        while i > 0:
            self._swap(i, 1)
            i -= 1
            self._shift_down(1, i)

    def build(self, collection):
        """
        创建堆
        :param collection:
        """
        self._heap = [None, *collection]
        self._size = len(collection)
        for i in range(self._size >> 1, 0, -1):
            self._shift_down(i, self._size)

    def _swap(self, i, j):
        """
        交换
        :param i:
        :param j:
        """
        temp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = temp

    def _shift_up(self, end):
        """
        自下而上堆化
        """
        while True:
            if end >> 1 >= 1 and self._heap[end] > self._heap[end >> 1]:
                self._swap(end, end >> 1)
                end = end >> 1
            else:
                break

    def _shift_down(self, start, end):
        """
        自上而下堆化
        """
        while True:
            max_pos = start
            if start << 1 <= end and self._heap[start] < self._heap[start << 1]:
                max_pos = start << 1

            if (start << 1) + 1 <= end and self._heap[max_pos] < self._heap[(start << 1) + 1]:
                max_pos = (start << 1) + 1
            if max_pos == start:
                break
            self._swap(max_pos, start)
            start = max_pos


def main():
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    print(heap.heap)

    heap.build([1, 2, 3, 4, 5, 6])
    print(heap.heap)

    # heap.sort()
    # print(heap.heap)

    heap.shift()
    print(heap.heap)


if __name__ == "__main__":
    main()
