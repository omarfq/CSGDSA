# Add a method to the LinkedList class that reverses the list

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self, head_node):
        self.head_node = head_node

    def reverse_list(self):
        current_node = self.head_node
        prev = None
        next = None
        while current_node:
            next = current_node.next_element
            current_node.next_element = prev
            prev = current_node
            current_node = next
        self.head_node = prev

    def print_list(self):
        current_node = self.head_node
        while current_node.next_element:
            print(current_node.data, end=' -> ')
            current_node = current_node.next_element
        print(current_node.data, '-> None')


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

node_1.next_element = node_2
node_2.next_element = node_3
node_3.next_element = node_4
node_4.next_element = node_5

linked_list = LinkedList(node_1)
linked_list.print_list()
linked_list.reverse_list()
linked_list.print_list()
