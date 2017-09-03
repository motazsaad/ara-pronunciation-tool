import argparse
import operator
import re

import phonetise_Arabic
from arutils import arabic_utils

parser = argparse.ArgumentParser(description='extracts dictionary and phones from a corpus')
parser.add_argument('-i', '--input', type=argparse.FileType(mode='r', encoding='utf-8'),
                    help='input file', required=True)
parser.add_argument('-p', '--project-name', type=str,
                    help='project name', required=True)
parser.add_argument('-s', '--s-tag', action='store_true',
                    help='the sentences include <s> tag')


def corpus2dictionary(corpus, project_name):
    pronunciation_dict = {}
    phones_list = set()
    phones_list.add('SIL')
    repeated_words = 0
    for line in corpus:
        if args.s_tag:
            sentence = re.search('<s>(.*)</s>', line).group(1)
        else:
            sentence = line
        words = sentence.split()
        for word in words:
            if word == '-':
                if word == "+MUSIC+" or word == "+NONTRANS+":
                    continue
                if not arabic_utils.remove_diacritics(word):
                    continue
                if word.isdigit():
                    continue
                phonetic = 'SIL'
                pronunciation_dict[word] = phonetic
            else:
                # u1: utterances_pronunciations_with_boundaries
                # u2: utterances_pronunciations
                # dic
                u1, u2, dic = phonetise_Arabic.my_phonetise(word)
                if len(u2) > 1:
                    repeated_words += 1
                phonetic = ' '.join(u2).replace('sil', '').strip()
                phonetic = phonetic.replace('TTTT', 'TT')
                phonetic = phonetic.replace('tttt', 'tt')
                phonetic = phonetic.replace('i0i0', 'i0')
                phonetic = phonetic.replace('nnnn', 'nn')
                if len(phonetic.replace(' ', '')) < len(word):
                    phonetic = ' '.join(list(phonetise_Arabic.arabicToBuckwalter(word)))
                clean_word = arabic_utils.remove_diacritics(word)
                if clean_word in pronunciation_dict:
                    if pronunciation_dict[clean_word] != phonetic:
                        pronunciation_dict[clean_word].append(phonetic)
                else:
                    pronunciation_dict[clean_word] = [phonetic]
                if word not in pronunciation_dict:
                    pronunciation_dict[word] = phonetic
            for ph in phonetic.split():
                phones_list.add(ph)

    sorted_dict = sorted(pronunciation_dict.items(), key=operator.itemgetter(1))
    phones_list = sorted(phones_list)

    with open(project_name + '.dic', mode='w', encoding='utf-8') as dict_writer:
        for w, ph in pronunciation_dict.items():
            dict_writer.write(w + "\t\t" + ph)
            dict_writer.write('\n')

    with open(project_name + '.phone', mode='w', encoding='utf-8') as phone_writer:
        for ph in phones_list:
            phone_writer.write(ph)
            phone_writer.write('\n')
    print('repeated_words = {}'.format(repeated_words))
    # print('error words: {}'.format(error_words))
    # with open(project_name + '.errors', mode='a') as error_writer:
    #     for w, p in error_words:
    #         error_writer.write("{}\t\t{}\n".format(w,p))


if __name__ == '__main__':
    args = parser.parse_args()
    corpus = args.input.readlines()
    proj_name = args.project_name
    corpus2dictionary(corpus, project_name=proj_name)
