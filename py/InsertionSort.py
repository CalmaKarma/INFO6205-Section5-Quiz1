from typing import List

DEBUG = False


class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self) -> List:
        """Sorts the array using Insertion Sort."""
        for i in range(1, len(self.array)):
            self.insert(i)
        return self.array

    def insert(self, i):
        """Inserts the 'Transition element' into its correct position in the sorted portion of the array."""
        for j in range(0, i):
            if self.array[j] > self.array[i]:
                for k in range(i, j, -1):
                    self.swap(k, k - 1)
                break

        if DEBUG:
            print(self.array)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]


if __name__ == '__main__':
    DEBUG = True
    InsertionSort([3, 3, 3, 1, 1, 2, 2]).sort()
