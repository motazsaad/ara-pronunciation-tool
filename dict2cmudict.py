import argparse
from alphabet_detector import AlphabetDetector

import phonetise_Arabic
import phonetise_Buckwalter

from arutils import arabic_utils

parser = argparse.ArgumentParser(description='convert dict to cmu dict format')
parser.add_argument('-i', '--input', type=argparse.FileType(mode='r', encoding='utf-8'),
                    help='input file', required=True)
parser.add_argument('-p', '--project-name', type=str,
                    help='project name', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    lines = args.input.readlines()
    proj_name = args.project_name
    cmu_dict = {}
    phones_set = set()
    ad = AlphabetDetector()
    for line in lines:
        if not line.strip():
            continue
        word = line.split()[0]
        phones = ' '.join(line.split()[1:])
        arabic_word = arabic_utils.remove_diacritics(phonetise_Arabic.buckwalterToArabic(word))
        print(word, arabic_word)
        if arabic_word in cmu_dict:
            cmu_dict[arabic_word].add(phones)
        else:
            cmu_dict[arabic_word] = {phones}
            for ph in phones.split():
                phones_set.add(ph)

    print('writing dic file')
    with open(proj_name + '.dic', mode='w', encoding='utf-8') as dict_writer:
        for w, ph in cmu_dict.items():
            if len(ph) == 1:
                dict_writer.write('{}\t\t{}\n'.format(w, ph.pop()))
            else:
                dict_writer.write('{}\t\t{}\n'.format(w, ph.pop()))
                for i, p in enumerate(ph):
                    dict_writer.write('{}({})\t\t{}\n'.format(w, (i + 1), p))
    print('writing phone file')
    with open(proj_name + '.phone', mode='w', encoding='utf-8') as phone_writer:
        for ph in phones_set:
            phone_writer.write(ph)
            phone_writer.write('\n')

    print('done!')





