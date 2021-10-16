class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self, head_node):
        self.head_node = head_node

    def delete_middle_node(self, node):
        node.data = node.next_element.data
        node.next_element = node.next_element.next_element

    def print_list(self):
        current_node = self.head_node
        while current_node.next_element:
            print(current_node.data, end=' -> ')
            current_node = current_node.next_element
        print(current_node.data, '-> None')
