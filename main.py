class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})

    def __repr__(self):
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        linkedlist = ''

        current = self.head

        while current:
            linkedlist += str(current.data)
            linkedlist += ' -><- '
            current = current.next

        linkedlist += 'None'

        return linkedlist

    def __repr__(self):
        return str(self.head)

    def print_list(self):
        return str(self.head)

    def insert_first(self, data):
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, next=self.head)
        self.head = node
        self.head.next.prev = self.head

    def insert_last(self, data):
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, prev=self.tail)
        self.tail.next = node

    def insert_at(self, index: int, data):
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

            counter = 0
            current = self.head

            while current and index > 0:
                pass

    def remove_first(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.head.prev = None

    def remove_last(self, data):
        if self.head is None and self.tail is None:
            return

        previous = self.tail.prev
        self.tail = previous
        self.tail.next = None

    def remove_at(self, index: int):
        if self.head is None and self.tail is None:
            return

    def reverse(self):
        if self.head is None and self.tail is None:
            return

    def get_first(self):
        if self.head is None:
            return

        return self.head

    def get_at(self, index: int):
        pass

    def __getitem__(self, index: int):
        pass

    def get_last(self):
        if self.head and self.tail is None:
            return

        return self.tail

    def length(self):
        if self.head is None and self.tail is None:
            return 0

        counter = 0
        current = self.head

        while current:
            current = current.next
            counter += 1

        return counter

    def __len__(self):
        return self.length()

    def clear(self):
        if self.head is None and self.tail is None:
            return

        self.head = None
        self.tail = None

    def for_each(self, fn):
        pass

    def find_index(self, index):
        pass

    def find(self):
        pass

    def contains(self):
        pass


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_first(2)
    linkedlist.insert_first(6)
    linkedlist.insert_first(11)
