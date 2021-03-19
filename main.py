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
        self.length = 0

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
        '''
        Inserts a node at the 0th position or first position in the linked list.
        The newly inserted node becomes the head of the list, and in the event
        that the list was empty the tail as well.
        '''
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            self.length += 1
            return

        node = Node(data, next=self.head)
        self.head = node
        self.head.next.prev = self.head
        self.length += 1

    def insert_last(self, data) -> None:
        '''
        Inserts a node at the last positions in the linked list. 
        The newly insersted node becomes the tail of the linked list.
        '''
        if self.head is None and self.tail is None:
            node = Node(data)
            self.head = node
            self.tail = node
            self.length += 1
            return

        node = Node(data, prev=self.tail)
        self.tail.next = node
        self.length += 1

    def insert_at(self, index: int, data) -> None:
        '''
        Inserts a node at any specified index within the linked list. 
        If the entered index is less than or equal to zero, the node will be entered in the
        0th position or the first and will become the head. If the index is greater than the size of
        the list, it will be inserted at the last position and become the tail of the list.
        '''
        if self.head is None and self.tail is None:
            self.insert_first(data)
            return

        if index <= 0:
            self.insert_first(data)
            return

        previous = self.get_at(index - 1)

        node = Node(data, prev=previous, next=previous.next)
        previous.next = node
        self.length += 1

    def remove_first(self) -> None:
        '''
        Removes the first node from the linked list. The node at the 1st position or the 
        second node become the first node and such also the head of the linked list.
        '''
        if self.head is None:
            return

        self.head = self.head.next
        self.head.prev = None
        self.length -= 1

    def remove_last(self, data) -> None:
        '''
        Removes the last node from the linked list. The node at n - 1 becomes the tail and the
        node that is last in the list.
        '''
        if self.head is None and self.tail is None:
            return

        previous = self.tail.prev
        self.tail = previous
        self.tail.next = None
        self.length -= 1

    def remove_at(self, index: int) -> None:
        '''
        Removes a Node at the specified index.
        '''
        if self.head is None and self.tail is None:
            return

        if index > self.length - 1 or index < 0:
            return

        if index == 0:
            self.remove_first()
            return

        previous = self.get_at(index - 1)
        previous.next = previous.next.next
        previous.next.prev = previous
        self.length -= 1

#! Write Tests for Sort
    def sort(self) -> None:
        '''
        Sorts the list by integer value, using bubble sort in ascending order.
        '''
        if self.head is None and self.tail is None:
            return

        current: Node = self.head
        next_node: Node = None

        while current:
            next_node = current.next

            while next_node:
                if next_node.data > current.data:
                    temp = current.data
                    current.data = next_node.data
                    next_node.data = temp

                next_node = next_node.next

            current = current.next

    def reverse(self) -> None:
        '''
        Reverses the doubly linked list.
        '''
        if self.head is None and self.tail is None:
            return

        current = self.head
        temp = None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

    def get_first(self) -> Node:
        '''
        Gets and returns the node at the 0th position in the list.
        The node is the head node.
        '''
        if self.head is None and self.tail is None:
            return

        return self.head

    def get_at(self, index: int):
        '''
        Gets the desired node at a certain index in the doubly linked list.
        If the index is greater than the list's size the last node will be returned.
        If the index is less than 0 the first node will be returned.
        '''

        if self.head is None and self.tail is None:
            return

        if index <= 0:
            return self.head

        current = self.head
        counter = 0

        while current.next is not None and counter < index:
            current = current.next
            counter += 1

        return current

    def __getitem__(self, index: int) -> Node:
        return self.get_at(index)

    def get_last(self) -> Node:
        '''
        Gets the last node in the linked list.
        '''

        if self.head is None and self.tail is None:
            return

        return self.tail

    def get_length(self) -> int:
        '''
        Gets the length or amount of nodes within the linked list.
        '''
        if self.head is None and self.tail is None:
            return 0

        return self.length

    def __len__(self) -> int:
        return self.length()

    def clear(self) -> None:
        '''
        Clears all nodes from the linked list.
        '''
        if self.head is None and self.tail is None:
            return

        self.head = None
        self.tail = None

    def for_each(self, fn) -> None:
        '''
        Iterates through the entire linked list calling the passed in function
        on the data of every node in the linked list. The passed function gets the 
        node's data passed as the first argument and the index of the node as the
        second argument.
        '''
        if self.head is None and self.tail is None:
            return

        current = self.head
        index = 0

        while current:
            new_data = fn(current.data, index)
            current.date = new_data
            current = current.next
            index += 1

    def find_index(self, data) -> int:
        '''
        Finds the first node with the specified data and returns the index of the node,
        in the event, no node houses the data passed in, -1 will be returned.
        '''
        if self.head is None and self.tail is None:
            return -1

        index = 0
        current = self.head

        while current:
            if current.data == data:
                return index

            current = current.next
            index += 0

        return -1

    def find(self, data) -> Node or None:
        '''
        Finds a specifi
        '''
        if self.head is None and self.tail is None:
            return

        current = self.head

        while current:
            if current.data == data:
                return current

            current = current.next

        return None

    def contains(self, data) -> bool:
        if self.head is None and self.tail is None:
            return False

        current = self.head

        while current:
            if current.data == data:
                return True

            current = current.next

        return False

    def print(self):
        linkedlist = self.__str__()
        print(linkedlist)

#! Test
    def is_empty(self) -> bool:
        if self.head is None and self.tail is None:
            return True

        return False


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_first(2)
    linkedlist.insert_first(6)
    linkedlist.insert_first(11)
    linkedlist.print()
    linkedlist.insert_last(22)
    linkedlist.insert_at(2, 22)
    linkedlist.insert_at(2242, 255)
    linkedlist.insert_at(-22, 4)

    linkedlist.print()

    linkedlist.get_at(3)
