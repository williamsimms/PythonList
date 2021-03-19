import unittest
from main import LinkedList, Node


class NodeTest(unittest.TestCase):
    def test_node_is_a_class(self):
        self.assertIsInstance(Node, object)

    def test_node_has_right_properties(self):
        node = Node('a', 'b', 'c')
        self.assertEqual(node.data, 'a')
        self.assertEqual(node.prev, 'b')
        self.assertEqual(node.next, 'c')

    def test_print_node(self):
        node = Node(2, None, None)
        self.assertEqual(
            str(node), "{'data': 2, 'prev': None, 'next': None}")


class LinkedListTest(unittest.TestCase):
    def test_list_is_a_class(self):
        self.assertIsInstance(LinkedList, object)

    def test_insert_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.head.data, 2)

    def test_length(self):
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.get_length(), 0)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_length(), 4)

    def test_get_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.head.data, 2)

    def test_get_last(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(4)
        self.assertEqual(str(linkedlist.get_last()),
                         "{'data': 4, 'next': None}")
        linkedlist.insert_first(2)
        self.assertEqual(str(linkedlist.get_last()),
                         "{'data': 4, 'next': None}")

    def test_clear(self):
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.get_length(), 0)
        linkedlist.insert_first(1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.head.data, 2)
        linkedlist.insert_first(6)
        self.assertEqual(linkedlist.get_length(), 3)
        linkedlist.clear()
        self.assertEqual(linkedlist.get_length(), 0)

    def test_remove_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        linkedlist.insert_first(5)
        linkedlist.insert_first(7)
        self.assertEqual(linkedlist.get_length(), 3)
        linkedlist.insert_first(3)
        self.assertEqual(linkedlist.get_length(), 4)
        linkedlist.remove_first()
        self.assertEqual(linkedlist.get_length(), 3)
        self.assertEqual(linkedlist.get_first().data, 7)
        linkedlist.remove_first()
        self.assertEqual(linkedlist.get_length(), 2)
        self.assertEqual(linkedlist.get_first().data, 5)

    def test_remove_first_none(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.get_length(), 1)
        linkedlist.remove_first()
        self.assertIsNone(linkedlist.head)

    def test_remove_last(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(2)
        linkedlist.insert_first(6)
        linkedlist.insert_first(8)
        self.assertTrue(linkedlist.get_length(), 3)
        self.assertTrue(linkedlist.get_last().data, 2)
        linkedlist.remove_last()
        self.assertEqual(linkedlist.get_length(), 2)
        self.assertTrue(linkedlist.get_last().data, 6)
        self.assertTrue(linkedlist.head.data, 8)

    def test_remove_last_no_error(self):
        linkedlist = LinkedList()
        linkedlist.remove_last()
        self.assertIsNone(linkedlist.head)

    def test_remove_last_node(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.get_length(), 1)
        linkedlist.remove_last()
        self.assertIsNone(linkedlist.head)

    def test_insert_last(self):
        linkedlist = LinkedList()
        linkedlist.insert_last(5)
        self.assertEqual(linkedlist.get_length(), 1)
        linkedlist.insert_first(7)
        linkedlist.insert_last(11)
        self.assertEqual(linkedlist.get_last().data, 11)

    def test_get_at(self):
        linkedlist = LinkedList()
        self.assertIsNone(linkedlist.get_at(10))

        linkedlist.insert_first(2)
        linkedlist.insert_first(6)
        linkedlist.insert_first(8)
        linkedlist.insert_first(4)

        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 8)
        self.assertEqual(linkedlist.get_at(2).data, 6)
        self.assertEqual(linkedlist.get_at(3).data, 2)

    def test_get_at_magic_method(self):
        linkedlist = LinkedList()
        linkedlist = LinkedList()
        self.assertIsNone(linkedlist[10])

        linkedlist.insert_first(2)
        linkedlist.insert_first(6)
        linkedlist.insert_first(8)
        linkedlist.insert_first(4)

        self.assertEqual(linkedlist[0].data, 4)
        self.assertEqual(linkedlist[1].data, 8)
        self.assertEqual(linkedlist[2].data, 6)
        self.assertEqual(linkedlist[3].data, 2)

    def test_remove_at_doesnt_crash_empty(self):
        linkedlist = LinkedList()
        linkedlist.remove_at(10)
        self.assertIsNone(linkedlist.head)

    def test_remove_at_doesnt_crash_out_of_bounds(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(3)
        linkedlist.remove_at(4)
        self.assertEqual(linkedlist.head.data, 3)

    def test_remove_at_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(4)
        linkedlist.insert_first(7)
        linkedlist.insert_first(3)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_at(0).data, 1)
        linkedlist.remove_at(0)
        self.assertEqual(linkedlist.get_at(0).data, 3)

    def test_remove_at_index(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(4)
        linkedlist.insert_first(7)
        linkedlist.insert_first(3)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_at(1).data, 3)
        linkedlist.remove_at(1)
        self.assertEqual(linkedlist.get_at(1).data, 7)

    def test_remove_at_last(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(4)
        linkedlist.insert_first(7)
        linkedlist.insert_first(3)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_last().data, 4)
        linkedlist.remove_at(3)
        self.assertEqual(linkedlist.get_last().data, 7)

    def test_insert_at_start_when_empty(self):
        linkedlist = LinkedList()
        linkedlist.insert_at(0, 10)
        self.assertEqual(linkedlist.get_first().data, 10)

    def test_insert_at_start_when_list_has_elements(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(4)
        linkedlist.insert_first(8)
        linkedlist.insert_first(9)
        linkedlist.insert_at(0, 10)
        self.assertEqual(linkedlist.get_first().data, 10)
        self.assertEqual(linkedlist.get_at(1).data, 9)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 4)

    def test_insert_at_middle(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(5)
        linkedlist.insert_first(7)
        linkedlist.insert_first(3)
        linkedlist.insert_first(2)
        linkedlist.insert_at(2, 11)
        self.assertEqual(linkedlist.get_at(0).data, 2)
        self.assertEqual(linkedlist.get_at(1).data, 3)
        self.assertEqual(linkedlist.get_at(2).data, 11)
        self.assertEqual(linkedlist.get_at(3).data, 7)
        self.assertEqual(linkedlist.get_at(4).data, 5)

    def test_insert_at_last(self):
        linkedlist = LinkedList()
        linkedlist.insert_last(5)
        linkedlist.insert_last(8)
        linkedlist.insert_last(3)
        linkedlist.insert_at(3, 14)
        self.assertEqual(linkedlist.get_at(0).data, 5)
        self.assertEqual(linkedlist.get_at(1).data, 8)
        self.assertEqual(linkedlist.get_at(2).data, 3)
        self.assertEqual(linkedlist.get_at(3).data, 14)

    def test_insert_at_when_out_of_bounds(self):
        linkedlist = LinkedList()
        linkedlist.insert_last(4)
        linkedlist.insert_last(11)
        linkedlist.insert_at(20, 17)
        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 11)
        self.assertEqual(linkedlist.get_at(2).data, 17)

    def test_for_eact(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(5)
        linkedlist.insert_first(7)
        linkedlist.insert_first(9)
        linkedlist.insert_first(11)

        linkedlist.for_each(lambda num, index: num + 10)

        self.assertTrue(linkedlist.get_at(0).data, 11)
        self.assertTrue(linkedlist.get_at(1).data, 9)
        self.assertTrue(linkedlist.get_at(2).data, 7)
        self.assertTrue(linkedlist.get_at(3).data, 5)

    def test_reverse(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(4)
        linkedlist.insert_first(8)
        linkedlist.insert_first(11)
        linkedlist.insert_first(5)

        self.assertEqual(linkedlist.get_at(0).data, 5)
        self.assertEqual(linkedlist.get_at(1).data, 11)
        self.assertEqual(linkedlist.get_at(2).data, 8)
        self.assertEqual(linkedlist.get_at(3).data, 4)
        self.assertEqual(linkedlist.head.data, 5)

        linkedlist.reverse()

        self.assertEqual(linkedlist.get_at(0).data, 4)
        self.assertEqual(linkedlist.get_at(1).data, 8)
        self.assertEqual(linkedlist.get_at(2).data, 11)
        self.assertEqual(linkedlist.get_at(3).data, 5)
        self.assertEqual(linkedlist.head.data, 4)

    def test_find_index(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(5)
        linkedlist.insert_first(1)
        linkedlist.insert_first(2)
        linkedlist.insert_first(3)
        linkedlist.insert_first(9)

        self.assertEqual(linkedlist.find_index(9), 0)
        self.assertEqual(linkedlist.find_index(3), 1)
        self.assertEqual(linkedlist.find_index(2), 2)
        self.assertEqual(linkedlist.find_index(1), 3)
        self.assertEqual(linkedlist.find_index(5), 4)
        self.assertEqual(linkedlist.find_index(11), -1)

    def test_contains(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        linkedlist.insert_first(2)
        linkedlist.insert_first(3)
        linkedlist.insert_first(4)
        linkedlist.insert_first(5)

        self.assertTrue(linkedlist.contains(1))
        self.assertTrue(linkedlist.contains(2))
        self.assertTrue(linkedlist.contains(3))
        self.assertTrue(linkedlist.contains(4))
        self.assertTrue(linkedlist.contains(5))
        self.assertFalse(linkedlist.contains(11))
        self.assertFalse(linkedlist.contains(9))
        self.assertFalse(linkedlist.contains(6))

    def test_find(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        linkedlist.insert_first(2)
        linkedlist.insert_first(5)
        linkedlist.insert_first(4)
        linkedlist.insert_first(9)

        self.assertEqual(linkedlist.find(1).data, 1)
        self.assertEqual(linkedlist.find(5).data, 5)
        self.assertEqual(linkedlist.find(2).data, 2)
        self.assertEqual(linkedlist.find(9).data, 9)
        self.assertIsNone(linkedlist.find(15))


if __name__ == '__main__':
    unittest.main()
