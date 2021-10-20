# Write an autocorrect function that attempts to replace the user's typo with a correct word
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

    def collect_all_words(self, node=None, word='', words=[]):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            if key == '*':
                words.append(word)
            else:
                self.collect_all_words(child_node, word + key, words)
        return words

    def autocorrect(self, word):
        current_node = self.root
        word_found_so_far = ''

        for char in word:
            if char in current_node.children:
                word_found_so_far += char
                current_node = current_node.children.get(char)
            else:
                return word_found_so_far + self.collect_all_words(current_node)[0]

        return word
