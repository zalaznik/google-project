

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 27
        self.sources_list


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _char_to_index(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        if ch == ' ':
            return 27
        return ord(ch) - ord('a')

    def insert(self, sub_string):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        current_level = self.root
        length = len(sub_string)

        for level in range(length):
            index = self._char_to_index(sub_string[level])

            # if current character is not present
            if not current_level.children[index]:
                current_level.children[index] = self.get_node()
            p_crawl = current_level.children[index]

        # mark last node as leaf
        current_level.sources_list = find_sources_of_best_complete_strings(sub_string)

    def search(self, string):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        current_level = self.root
        length = len(string)
        for level in range(length):
            index = self._char_to_index(string[level])
            if not current_level.children[index]:
                return []
            current_level = current_level.children[index]

        return current_level.sources_list
