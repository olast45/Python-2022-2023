import random


class RandomQueue:

    def __init__(self, size=15):
        self.size = size
        self.data = []

    def insert(self, item):  # wstawia element w czasie O(1)
        self.data.append(item)

    def remove(self):  # zwraca losowy element w czasie O(1)
        element_index = random.randint(0, len(self.data) - 1)
        self.data[element_index], self.data[-1] = self.data[-1], self.data[element_index]
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return self.size == len(self.data)

    def clear(self):  # czyszczenie listy
        self.data = []


