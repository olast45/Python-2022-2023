class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def search(self, data):  # klasy O(n)
        if self.is_empty():
            raise ValueError("pusta lista")
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def find_min(self):  # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        current_node = self.head
        min_data = current_node.data
        while current_node is not None:
            if min_data > current_node.data:
                min_data = current_node.data
            current_node = current_node.next
        return min_data

    def find_max(self): # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        current_node = self.head
        max_data = current_node.data
        while current_node is not None:
            if max_data < current_node.data:
                max_data = current_node.data
            current_node = current_node.next
        return max_data

    def reverse(self):  # Odwracanie kolejności węzłów na liście.
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev