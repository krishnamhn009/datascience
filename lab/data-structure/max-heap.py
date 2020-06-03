import sys


class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.Front = 1

    # retrun parent's pos
    def parent(self, pos):
        return pos // 2

    # retrun left child's pos
    def lefChild(self, pos):
        return 2 * pos

        # retrun right child's pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if pos >= (self // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def maxHeapify(self, pos):
        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (
                self.Heap[pos] < self.Heap[self.leftChild(pos)]
                or self.Heap[pos] < self.Heap[self.rightChild(pos)]
            ):
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(
                " PARENT : "
                + str(self.Heap[i])
                + " LEFT CHILD : "
                + str(self.Heap[2 * i])
                + " RIGHT CHILD : "
                + str(self.Heap[2 * i + 1])
            )

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped


# Driver Code
if __name__ == "__main__":
    print("The maxHeap is ")
    minHeap = MaxHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)

    minHeap.Print()
    print("The Max val is " + str(minHeap.extractMax()))
