import operator
import re
import string

from alphabet_detector import AlphabetDetector

arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)


def remove_diacritics(text):
    text = re.sub(arabic_diacritics, '', text)
    return text


def remove_punctuation(s):
    translator = str.maketrans('', '', string.punctuation + "،" + "؛" + "؟" + "«" + "»" + '–')
    return s.translate(translator)


def get_none_arabic_words(text):
    none_arabic = list()
    ad = AlphabetDetector()
    for word in text.split():
        if not ad.is_arabic(word):
            none_arabic.append(word)
    return none_arabic


def keep_only_arabic(text):
    ad = AlphabetDetector()
    clean_lines = list()
    for line in text.splitlines():
        clean_line = list()
        for word in line.split():
            if ad.is_arabic(word):
                if word.isalpha():
                    clean_line.append(word)
        clean_lines.append(' '.join(clean_line))
    return '\n'.join(clean_lines)


def remove_links(text):
    # return re.sub(r'\s*(?:https?://)?www\.\S*\.[A-Za-z]{2,5}\s*', ' ', text, flags=re.MULTILINE).strip()
    # return re.sub(r'^https?:\/\/.*[\r\n]*', '', clean_text, flags=re.MULTILINE)
    return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)


def remove_empty_lines(text):
    lines = [s.rstrip() for s in text.split("\n") if s.rstrip()]
    return '\n'.join(lines)


def find_most_freq(words, topn):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    sorted_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

    top = [list(i) for i in sorted_freq[:topn]]  # list of lists
    return sorted_freq[:topn]


def add_s_tag(input_corpus, corpus_outfile):
    corpus_writer = open(corpus_outfile, mode='w')
    for line in input_corpus:
        corpus_writer.write("<s> " + line + " </s>\n")


def remove_repeating_char(text):
    # return re.sub(r'(.)\1+', r'\1', text)     # keep only 1 repeat
    return re.sub(r'(.)\1+', r'\1\1', text)  # keep 2 repeat
