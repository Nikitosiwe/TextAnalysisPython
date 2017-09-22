import re
import pymorphy2 as pym

#Метод принимает текст (который подлжежит анализу). И проверяет его корректность
#для дальнейшей работы с ним. Например текст не должен состоять из одних пробелов,
#табуляций и абзацев
def checkAnalysisText(text):
    if isinstance(text, str):
        if re.search('\S',text)!=None:
            return True
        else:
            return False
    else:
        print("checkAnalysisText - Это не текст")


#Метод разбивает строку на слова и возвращает словарь найденых слов с их индексами в строке
#{'Слова':[(начальный индекс вхождения 1, конечный индекс вхождения 1),(начальный индекс вхождения 2, конечный индекс вхождения 2),...]}
def getWordsFromString(text):
    #Убирает лишние символы и сдвигает индексы соответственно
    def temp(tp):
        r = re.finditer('\w+',tp[2])
        s = next(r)
        return (tp[0]+s.start(0), tp[0]+s.start(0)+(s.end(0)-s.start(0)), s.group(0))

    tmp ={}
    for m in re.finditer('[\W|\s]?(\w+)[\W|\s]?', text):
        w = temp((m.start(0), m.end(0), m.group(0)))
        if w[2] in tmp.keys():
            tmp[w[2]].append((w[0],w[1]))
        else:
            tmp[w[2]]=[(w[0],w[1])]

    return tmp


#Метод ищет вхождения слова в строке. return ('Cлово',[позиция в строке 1, позиция в строке 2, ....])
def searchWord(word, s):
    """
    i=0
    lst = []
    while(i!=-1):
        i = s.find(word, i+1)
        if i != -1:
            lst.append(i)
        else:
            continue
    """

    return [(m.start(0), m.end(0)) for m in re.finditer('[\s]+'+word+'[\s]+', s)]


#Метод выделяет из списка слов значемые (существительные)
# и стоп слова (Союзы, Местоимения, Предлоги, Частицы, Междометия, Цифры)
# и иностранные слова
def getMorphWords(words):
    znach =[]
    Nznach=[]
    ltn =[]
    morph = pym.MorphAnalyzer()
    for w in words:
        if 'NOUN' in morph.parse(w)[0].tag:
            znach.append(w)
        elif ('CONJ' or 'NPRO' or 'PREP' or 'PRCL' or 'INTJ' or  'NUMR') in morph.parse(w)[0].tag:
            Nznach.append(w)
        elif None == morph.parse(w)[0].tag.POS:
            ltn.append(w)
    return (znach, Nznach, ltn)

# Метод возвращает все аналитические параметры текста
def analysisText(text):
    words = getWordsFromString(text)

    #Количество символов
    symbol_count = len(text)

    #Количество символов без пробелов
    symbol_count_2 =len(re.sub('\s+','',text))

    #Количество слов
    word_count = sum([len(x) for x in words.values()])

    #Количество букв
    letter_count = sum([len(w) for w in words.keys()])

    #Количество уникальных слов
    word_count_2 = len(words.keys())

    morphWords = getMorphWords(words)

    #количество значимых слов
    word_count_3 = len(morphWords[0])

    #Количество стоп-слов
    word_count_4 = len(morphWords[1])

    try:
        #Водность текста
        water = sum([len(words[mw]) for mw in morphWords[1]]) / sum([len(words[mw]) for mw in morphWords[0]]) * 100
    except ZeroDivisionError:
        water = 100

    #Количество иностранных слов
    ltn_count = len(morphWords[2])


    return (symbol_count, symbol_count_2, word_count, letter_count, word_count_2, word_count_3, word_count_4, water, ltn_count)