from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def open_file (file):
    with open(file) as file:
        return file.read()
    
def remove_punctuation(file):
    no_punct = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in file:
        if char not in punctuations:
            no_punct+= char
    return no_punct

def lowercase_and_split(file):
    x = file.lower().split(" ")
    return x

def remove_stops (file):
    stops_removed = []
    i = 0
    while i < len(file):
        if file[i] not in STOP_WORDS:
            stops_removed.append(file[i])
        i+= 1
    return stops_removed

def count_and_sort (file):
    word_count = dict(Counter(file))
    word_count = {k: v for k, v in sorted(word_count.items(), key = lambda item: item[1], reverse=True)}
    return word_count

def render_dict (file):
    for word, num in file.items():
        print(f"{word} | {num} " + num * "*")

# render_dict(count_and_sort(remove_stops(lowercase_and_split(remove_punctuation(open_file())))))

def print_word_freq(file):
    print(f"Word frequencies in file: {file}")
    text = open_file(file)
    text = remove_punctuation(text)
    text = lowercase_and_split(text)
    text = remove_stops(text)
    text = count_and_sort(text)
    render_dict(text)

print_word_freq('seneca_falls.txt')
print_word_freq('emancipation_proclamation.txt')


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
