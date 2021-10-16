# Add a method to the LinkedList class that returns the last element of the list

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self, head_node):
        self.head_node = head_node

    def return_last(self):
        current_node = self.head_node
        while current_node.next_element:
            current_node = current_node.next_element
        return current_node.data


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

node_1.next_element = node_2
node_2.next_element = node_3
node_3.next_element = node_4

linked_list = LinkedList(node_1)
print(linked_list.return_last())
