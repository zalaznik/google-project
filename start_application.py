from complete_to_sentences_online import init_system, get_best_k_completions

k = 5


def print_completions(the_completions):
    m = min(len(the_completions), k)

    if not the_completions:
        print("no suggestions :(")
    else:
        print(f"Here are the {m} suggestions")
        for i in range(1, m + 1):
            print(f"{i}. {completions[i - 1]}")
        print(f"\n{input_}", end="")


if __name__ == "__main__":
    print("\nLoading the files and preparing the system...")
    init_system()
    print("the system is ready \n")
    while True:
        input_ = input("please enter a text\n")
        if input_:
            while input_[-1] != '#':
                # validate_input()
                completions = get_best_k_completions(input_)
                print_completions(completions)
                input_ += input()
