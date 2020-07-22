from find_complete_sentences_online import init_system, get_best_k_completions


if __name__ == "__main__":
    print("starting...\n")
    init_system()
    print("finished\n")
    while True:
        input_ = input("please enter...\n")
        while input_[-1] != '#':
            # validate_input()
            for completions in get_best_k_completions(input_):
                print(f"completions: {completions}\n{input_}")
            input_ += input()
