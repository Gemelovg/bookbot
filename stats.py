def get_num_words(filepath):
    line = []
    with open(filepath) as f:
        lines = f.read()
        line = len(lines.split())
    return line


def number_of_chars(filepath):
    char_d = {}
    with open(filepath) as f:
        lines = f.read().lower()
        for chars in lines:
            if chars in char_d:
                char_d[chars] = char_d[chars] + 1
            else:
                char_d[chars] = 1
    # print(char_d)
    return char_d


def sorted_number_of_chars(dict):
    (sorted(dict.items()))
    return dict
