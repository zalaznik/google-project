from .dict_of_sentences import sentences_dict
from utils import normal_string


class TrieNode:

    def __init__(self, father):
        self.children = [None] * (26+1)
        self.sources_list = []
        self.father = father


class Trie:

    def __init__(self):
        self.root = self.get_node(None)

    def get_node(self, father):
        return TrieNode(father)

    def char_to_index(self, ch):
        if ch == ' ':
            return 26
        return ord(ch) - ord('a')

    def insert(self, sub_string, key):
        current_level = self.root
        length = len(sub_string)

        for level in range(length):
            index = self.char_to_index(sub_string[level])

            if not current_level.children[index]:
                current_level.children[index] = self.get_node( current_level)
            current_level = current_level.children[index]

        if len(current_level.sources_list) < 5 and key not in current_level.sources_list:
            current_level.sources_list.append(key)

    def normal_search(self, node, string):

        # the brother is not exist
        if node is None:
            return [], None, 0

        for level in range(0, len(string)):
            index = self.char_to_index(string[level])

            if not node.children[index]:
                return [], node, level

            node = node.children[index]

        return node.sources_list, node.father, len(string) - 1

# need to add the search for the case of add a letter or remove a letter
# now this func is works for the normal case and for the case of change a letter
    def search(self, sub_string):

        # first searching for the simple case
        complete_list, father, traveled_length = self.normal_search(self.root, sub_string)

        while father and len(complete_list) < 5:

            # case of exchange a letter
            for child in father.children:
                current_complete_list, _, _ = self.normal_search(child, sub_string[traveled_length+1:])

                for item in current_complete_list:
                    if item not in complete_list:
                        complete_list.append(item)

                if len(complete_list) >= 5:
                    return complete_list[:5]

            # case of add a letter
            current_complete_list, _, _ = self.normal_search(father, sub_string[traveled_length + 1:])

            for item in current_complete_list:
                if item not in complete_list:
                    complete_list.append(item)

            if len(complete_list) >= 5:
                return complete_list[:5]

            # case of remove a letter
            for child in father.children:
                current_complete_list, _, _ = self.normal_search(child, sub_string[traveled_length:])

                for item in current_complete_list:
                    if item not in complete_list:
                        complete_list.append(item)

                if len(complete_list) >= 5:
                    return complete_list[:5]

            traveled_length -= 1
            father = father.father

        return complete_list


substrings_trie = Trie()


def find_all_substrings(string):
    len_string = len(string)

    for i in range(0, len_string):
        for j in range(i + 1, len_string + 1):
            yield string[i: j]


def init_substring_trie():
    for key, sentence in sentences_dict.items():
        for substring in find_all_substrings(normal_string(sentence.completed_sentence)):
            substrings_trie.insert(substring, key)
