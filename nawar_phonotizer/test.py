from nawar_phonotizer import diphones


# diphonesresults, diphonesTypes = diphones.diphones("test.txt")
#
# # for d in diphonesresults:
# #     print(d)
#
# print('---------------------')
# for d in diphonesTypes:
#     print(d)


from nawar_phonotizer import phonetise_Arabic
#phonemes = phonetise_Arabic.phonetise("السلام عليكم انا اسمي معتز")
#print(phonemes)

txt1  = "وَرَجَّحَ التَّقْرِيرُ الَّذِي أَعَدَّهُ مَعْهَدُ أَبْحَاثِ هَضَبَةِ التِّبِتِ فِي الْأَكَادِيمِيَّةِ الصِّينِيَّةِ لِلْعُلُومِ - أَنْ تَسْتَمِرَّ دَرَجَاتُ الْحَرَارَةِ وَمُسْتَوَيَاتُ الرُّطُوبَةِ فِي الْإِرْتِفَاعِ طَوَالَ هَذَا الْقَرْنْ"
txt2 = "السلام عليكم انا اسمي معتز"
for word in txt1.split():
    u1, u2, dic = phonetise_Arabic.my_phonetise(word)
    #print('word: {}\t\tu1: {}\t\tu2: {}\t\tdic: {}'.format(word, u1, u2, dic))
    phonetic = u2[0].replace('sil', '').strip()
    print('word: {}\t\tphonetic: {}'.format(word, phonetic))



#print(phonetise_Arabic.phonetise(txt))

from nawar_phonotizer import phonetise_Buckwalter
#print(phonetise_Buckwalter.work("AlslAm Elykm"))