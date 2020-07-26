from .auto_complete_data import AutoCompleteData
import glob


sentences_dict = {}

# need to change the read to be from all the files


def init_sentences_dict():
    # read sentences from files
    for filename in glob.iglob("data_technology_texts/" + 'bugs.txt', recursive=True):
        with open(filename, mode='r', encoding='utf-8') as f:
            sentences = f.readlines()
            sentences = [x.strip() for x in sentences]
            for i in range(len(sentences)):
                sentences_dict[i] = AutoCompleteData(sentences[i], filename.rpartition("/")[-1].rpartition(".")[0])
