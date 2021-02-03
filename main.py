class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})

    def __repr__(self) -> str:
        return str({'data': self.data, 'prev': self.prev, 'next': self.next})


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def __str__(self) -> str:
        linkedlist = ''

        current = self.head

        while current:
            linkedlist += str(current.data)
            linkedlist += ' -><- '
            current = current.next

        linkedlist += 'None'

        return linkedlist

    def __repr__(self) -> str:
        return str(self.head)

    def insert_first(self, data) -> None:
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, next=self.head)
        self.head = node
        self.head.next.prev = self.head

    def insert_last(self, data) -> None:
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data, prev=self.tail)
        self.tail.next = node

    def insert_at(self, index: int, data) -> None:
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        counter = 0
        current = self.head

        while current and counter != index:
            if counter == index:
                break

            current = current.next

        node = Node(data, prev=current, next=current.next)
        current.next = node

    def remove_first(self) -> None:
        if self.head is None:
            return

        self.head = self.head.next
        self.head.prev = None

    def remove_last(self, data) -> None:
        if self.head is None and self.tail is None:
            return

        previous = self.tail.prev
        self.tail = previous
        self.tail.next = None

    def remove_at(self, index: int) -> None:
        if self.head is None and self.tail is None:
            return

    def reverse(self) -> None:
        if self.head is None and self.tail is None:
            return

    def get_first(self) -> Node:
        if self.head is None:
            return

        return self.head

    def get_at(self, index: int) -> Node:
        if self.head is None and self.tail is None:
            return

        current = self.head

        while current and index > 0:
            current = current.next
            index -= 1

        return current

    def __getitem__(self, index: int) -> Node:
        return self.get_at(index)

    def get_last(self) -> Node:
        if self.head is None and self.tail is None:
            return

        return self.tail

    def length(self) -> int:
        if self.head is None and self.tail is None:
            return 0

        counter = 0
        current = self.head

        while current:
            current = current.next
            counter += 1

        return counter

    def __len__(self) -> int:
        return self.length()

    def clear(self) -> None:
        if self.head is None and self.tail is None:
            return

        self.head = None
        self.tail = None

    def for_each(self, fn) -> None:
        if self.head is None and self.tail is None:
            return

        current = self.head

        while current:
            current = current.next

    def find_index(self, index) -> int:
        pass

    def find(self) -> Node:
        pass

    def contains(self) -> bool:
        pass


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_first(2)
    linkedlist.insert_first(6)
    linkedlist.insert_first(11)
