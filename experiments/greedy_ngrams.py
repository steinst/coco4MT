import sys

input_file = sys.argv[1]
max_allowed = sys.argv[2]
output_file = input_file + '.ngrams_min' + str(max_allowed)

unigrams_dict = {}
bigrams_dict = {}
trigrams_dict = {}


def unigrams(line):
    global unigrams_dict
    unigram_score = 0
    for token in line.split():
        if token not in unigrams_dict:
            unigram_score += 1
        elif unigrams_dict[token] < int(max_allowed):
            unigram_score += 1
    return unigram_score


def add_unigrams(line):
    global unigrams_dict
    for token in line.split():
        if token not in unigrams_dict:
            unigrams_dict[token] = 1
        else:
            unigrams_dict[token] += 1


def bigrams(line):
    global bigrams_dict
    bigram_score = 0
    bigram_array = ['','']
    for token in line.split():
        bigram_array[0] = bigram_array[1]
        bigram_array[1] = token
        if '_'.join(bigram_array) not in bigrams_dict:
            bigram_score += 1
        elif bigrams_dict['_'.join(bigram_array)] < int(max_allowed):
            bigram_score += 1
    return bigram_score


def add_bigrams(line):
    global bigrams_dict
    bigram_array = ['','']
    for token in line.split():
        bigram_array[0] = bigram_array[1]
        bigram_array[1] = token
        if '_'.join(bigram_array) not in bigrams_dict:
            bigrams_dict['_'.join(bigram_array)] = 1
        else:
            bigrams_dict['_'.join(bigram_array)] += 1


def trigrams(line):
    global trigrams_dict
    trigram_score = 0
    trigram_array = ['','','']
    for token in line.split():
        trigram_array[0] = trigram_array[1]
        trigram_array[1] = trigram_array[2]
        trigram_array[2] = token
        if '_'.join(trigram_array) not in trigrams_dict:
            trigram_score += 1
        elif trigrams_dict['_'.join(trigram_array)] < int(max_allowed):
            trigram_score += 1
    return trigram_score


def add_trigrams(line):
    global trigrams_dict
    trigram_array = ['','','']
    for token in line.split():
        trigram_array[0] = trigram_array[1]
        trigram_array[1] = trigram_array[2]
        trigram_array[2] = token
        if '_'.join(trigram_array) not in trigrams_dict:
            trigrams_dict['_'.join(trigram_array)] = 1
        else:
            trigrams_dict['_'.join(trigram_array)] += 1


file_open = open(input_file, 'r')
file_lines = file_open.readlines()

lines = []

for line in file_lines:
    lines.append(line.strip())

with open(output_file, 'w') as fo:
    while len(lines) > 0:
        max_score = 0
        max_line = ''
        for line in lines:
            curr_score = 0
            curr_score += unigrams(line)
            curr_score += bigrams(line)
            curr_score += trigrams(line)
            if curr_score > max_score:
                max_score = curr_score
                max_line = line
        fo.write(max_line + '\t' + str(len(max_line.split())) + '\t' + str(unigrams(max_line)) + '\t' + str(bigrams(max_line)) + '\t' + str(trigrams(max_line)) + '\t' + str(max_score) + '\n')
        add_unigrams(max_line)
        add_bigrams(max_line)
        add_trigrams(max_line)
        lines.remove(max_line)
        if max_score == 0:
            break

file_open.close()