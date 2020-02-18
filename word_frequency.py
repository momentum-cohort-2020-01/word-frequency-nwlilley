from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


with open('seneca_falls.txt') as file:
    text = file.read()

no_punct = ""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for char in text:
    if char not in punctuations:
        no_punct+= char

lowered = no_punct.lower()

list_words = lowered.split(" ")

print(len(list_words))
stops_removed = []
i = 0
while i < len(list_words):
    if list_words[i] not in STOP_WORDS:
        stops_removed.append(list_words[i])
    i+= 1

# for word in stops_removed:



word_count = Counter(stops_removed)
# print(word_count)
word_dict = dict(word_count)
word_dict = {k: v for k, v in sorted(word_dict.items(), key = lambda item: item[1], reverse=True)}

print(word_dict)

for word, num in word_dict.items():
    print(f"{word} | {num} " + num * "*")

# def print_word_freq(file):
    
#     pass


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
