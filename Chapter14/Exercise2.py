class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    def __init__(self, head_node, last_node):
        self.head_node = head_node
        self.last_node = last_node

    def print_in_reverse(self):
        current_node = self.last_node
        while current_node.previous_element:
            print(current_node.data, end=' -> ')
            current_node = current_node.previous_element
        print(current_node.data, '-> None')


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

node_1.next_element = node_2
node_2.previous_element = node_1

node_2.next_element = node_3
node_3.previous_element = node_2

node_4.previous_element = node_3

doubly_linked_list = DoublyLinkedList(node_1, node_4)
doubly_linked_list.print_in_reverse()
