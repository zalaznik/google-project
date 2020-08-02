from meta_data.dict_of_sentences import sentences_dict, init_sentences_dict
from meta_data.trie_of_substrings import substrings_trie, init_substring_trie


def init_system():
    init_sentences_dict()
    init_substring_trie()


def get_best_k_completions(string):
    ids_and_offsets_completions_list = substrings_trie.search(string)
    sentences_and_offsets_completions_list = []

    for completion in ids_and_offsets_completions_list:
        sentences_and_offsets_completions_list.append((sentences_dict[completion[0]], completion[1]))

    return sentences_and_offsets_completions_list

