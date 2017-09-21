import re

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