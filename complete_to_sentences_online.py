from meta_data.dict_of_sentences import sentences_dict, init_sentences_dict
from meta_data.trie_of_substrings import substrings_trie, init_substring_trie


def init_system():
    init_sentences_dict()
    init_substring_trie()


def get_best_k_completions(string):
    sources_list = substrings_trie.search(string)
    result_as_list = []

    for source in sources_list:
        result_as_list.append(sentences_dict[source])

    return result_as_list

