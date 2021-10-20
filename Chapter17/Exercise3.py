# Write a function that traverses each node of a trie and prints each key, including all "*"
# keys

class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def print_key(self, node=None):
        current_node = self.root or node
        for key, childNode in current_node.children.items():
            print(key)
            if key != '*':
                self.traverse(childNode)
