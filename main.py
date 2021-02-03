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
            linkedlist += int(current.data)
            linkedlist += ' => '
            current = current.next

        linkedlist += 'None'

    def __repr__(self):
        return str(self.head)

    def print(self):
        return str(self.head)

    def insert_first(self, data):
        if not self.head:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, next=self.head)
        self.head = node

    def insert_last(self, data):
        pass


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_first(2)
