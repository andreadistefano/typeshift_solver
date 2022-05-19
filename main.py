import itertools

with open("words_alpha.txt", "r") as f:
    all_words = set(f.read().split())

with open("puzzle.txt", "r") as f:
    splitted_columns = list(list(x) for x in f.read().split())

possible_words = set([''.join(p) for p in itertools.product(*splitted_columns)])
correct_words = possible_words.intersection(all_words)

print(sorted(correct_words))