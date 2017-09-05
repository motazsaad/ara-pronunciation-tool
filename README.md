# ara-pronunciation-tool

A python tool that converts Arabic diacritised text to a sequence of phonemes and create a pronunciation dictionary. 

This code  is based on https://github.com/nawarhalabi/Arabic-Phonetiser

Modifications mainly make the code in https://github.com/nawarhalabi/Arabic-Phonetiser compatible with python 3, and provide easy to use cmd tool to build the pronunciation dictionary. 

The pronounciation is generated based on Buckwalter transliteration
see https://en.wikipedia.org/wiki/Buckwalter_transliteration and http://www.qamus.org/transliteration.htm for more information 


## test on text with diacritics 
```
python phonetise_Arabic.py -i nawar_corpus_tashkeel.txt

python dict2cmudict.py -i nawar_corpus_tashkeel.txt.dict -p nawar_bw_tashkeel

```  

## test on text without diacritics 
```
python phonetise_Arabic.py nawar_corpus.txt

python dict2cmudict.py -i dict -p nawar_bw_

```  

## test with corpus2cmudict.py on text with diacritics 
```
python corpus2cmudict.py -i nawar_corpus_tashkeel.txt -p nawar_bw_tashkeel
```

## test with corpus2cmudict.py on text without diacritics 
```
python corpus2cmudict.py -i nawar_corpus_plain.txt -p nawar_bw_plain
```
 