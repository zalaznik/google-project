from complete_to_sentences import find_sources_of_best_complete_strings
from dict_of_sentences import sentences_dict


class TrieNode:

    def __init__(self):
        self.children = [None] * 27
        self.sources_list = []


class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):

        if ch == ' ':
            return 27
        return ord(ch) - ord('a')

    def insert(self, sub_string):
        current_level = self.root
        length = len(sub_string)

        for level in range(length):
            index = self._char_to_index(sub_string[level])

            if not current_level.children[index]:
                current_level.children[index] = self.get_node()
            current_level = current_level.children[index]

        current_level.sources_list = find_sources_of_best_complete_strings(sub_string)

    def search(self, string):
        current_level = self.root
        length = len(string)
        for level in range(length):
            index = self._char_to_index(string[level])
            if not current_level.children[index]:
                return []
            current_level = current_level.children[index]

        return current_level.sources_list


substrings_trie = Trie()


def find_all_substrings(string):
    len_string = len(string)

    for i in range(0, len_string):
        for j in range(i, len_string + 1):
            yield string[i: j]


def init_substring_trie():
    for sentence in sentences_dict.values():
        for substring in find_all_substrings(sentence):
            substrings_trie.insert(substring)



