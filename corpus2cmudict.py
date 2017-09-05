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
    for line in corpus:
        if args.s_tag:
            sentence = re.search('<s>(.*)</s>', line).group(1)
        else:
            sentence = line
        words = sentence.split()
        for word in words:
            pronunciations = phonetise_Arabic.phonetise_word(word)
            for pronunciation in pronunciations:
                for phone in pronunciation.split():
                    phones_list.add(phone)
            clean_word = arabic_utils.remove_diacritics(word)
            if clean_word in pronunciation_dict:
                for pronunciation in pronunciations:
                    pronunciation_dict[clean_word].add(pronunciation)
            else:
                pronunciation_dict[clean_word] = set()
                for pronunciation in pronunciations:
                    pronunciation_dict[clean_word].add(pronunciation)

    print('writing dic file')
    with open(proj_name + '.dic', mode='w', encoding='utf-8') as dict_writer:
        for w, phones in sorted(pronunciation_dict.items()):
            for i, phone in enumerate(phones):
                if i == 0:
                    dict_writer.write('{}\t\t{}\n'.format(w, phone))
                else:
                    dict_writer.write('{}({})\t\t{}\n'.format(w, (i + 1), phone))

    print('writing phone file')
    with open(proj_name + '.phone', mode='w', encoding='utf-8') as phone_writer:
        for ph in sorted(phones_list):
            phone_writer.write(ph)
            phone_writer.write('\n')


if __name__ == '__main__':
    args = parser.parse_args()
    corpus = args.input.readlines()
    proj_name = args.project_name
    corpus2dictionary(corpus, project_name=proj_name)
